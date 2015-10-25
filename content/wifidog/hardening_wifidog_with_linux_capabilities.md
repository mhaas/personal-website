Title: Hardening Wifidog with Linux capabilities
Date: 2015-04-09
lang: en
tags: wifidogs, oss, capabilities, hardening

## Hardening Wifidog ##

Wifidog run as root and that's bad. The omnipotent superuser
allows Wifidog to do absolutely everything on (and to) the system. An
attacker who is able to [remotely execute arbitrary code](https://en.wikipedia.org/wiki/Arbitrary_code_execution)
can easily take over the whole system.

## Capable of Less ##

Enter Linux capabilities ([*man 7 capabilities*](http://linux.die.net/man/7/capabilities)).
Capabilities divide the full set of privileges into individual units. By dropping unneeded
capabilities such as the privilege to bypass file permission checks (**CAP\_DAC_\_OVERRIDE**),
it becomes much harder for the hypothetical attacker to cause mischief on the system.
In addition to arbitrary remote execution, the attacker would have [to escalate their
privileges](https://en.wikipedia.org/wiki/Privilege_escalation). This is a lot harder.

## The Art of Minimalism ##

Wifidog needs two privileges:

* **CAP\_NET\_RAW** to determine the IP address of its network interfaces
* **CAP\_NET\_ADMIN** to modify firewall rules

So, the whole thing should be easy. We start as root and use *libcap* to drop
all privileges but these two. Afterwards, we switch to a (traditionally) unprivileged
user because root can still read (and write!) its own files. Note that
unprivileged here means an UID other than 0. Running as UID 0 with dropped capabilities would be
problem because an attacker could still place a shell script in */etc/cron.d/*
which would then be executed by cron running as root with the full set of
capabilities.

It doesn't work out that way. Of course.

## The Devil, the Details and execve() ##

Linux knows thread-based capabilites and file-based capabilities. Wifidog internally
executes *iptables* to set firewall rules. Unfortunately, **subprocesses do not inherit
capabilities by default**. Even if we add **CAP\_NET\_RAW** and **CAP\_NET\_ADMIN**
to the **INHERITABLE** set for the wifidog process, Linux will still perform
transformations of the capability sets  based on the file capabilities of the executables
invoked as a subprocess. The transformation rules are as follows (straight from the man page):

     During an execve(2), the kernel calculates the new capabilities of the process
     using the following algorithm:

           P'(permitted) = (P(inheritable) & F(inheritable)) |
                           (F(permitted) & cap_bset)

           P'(effective) = F(effective) ? P'(permitted) : 0

           P'(inheritable) = P(inheritable)    [i.e., unchanged]

       where:

           P         denotes the value of a thread capability set before the execve(2)

           P'        denotes the value of a capability set after the execve(2)

           F         denotes a file capability set

           cap_bset  is the value of the capability bounding set (described below).


We care about *P'(effective)*. Working backwards, we see that the effective capabilities of the subprocess
come from the **PERMITTED** set of the subprocess IFF the **EFFECTIVE** file capability *F'(effective)* is set.
To set up the prerequisite *P'(permitted)* set, the intersection of the **INHERITABLE** sets for Wifidog
and the subprocess, *iptables*, is taken.

To make things finally work, we use */usr/bin/setcap* to set the file-based capabilities:

        setcap cap_net_admin,cap_net_raw+ei /usr/bin/xtables-multi

On a side note, if you add a capability to both  **PERMITTED** and **EFFECTIVE** set of an executable,
the process gets the capability in its **PERMITTED** set. In practice, anyone could then run iptables:


        setcap cap_net_admin,cap_net_raw+ep /usr/bin/xtables-multi

Don't do that. It's mainly useful for tools like *ping* which would otherwise be SETUID0.

    $ getcap /usr/bin/ping
    /usr/bin/ping = cap_net_raw+ep


## Minimalistic Capability Sets and Minimalistic Environments ##

That's quite the effort to reduce the set of privileges. It's confusing that
capability inheritance does not work out of the box and needs special treatment
for executables running as subprocesses. I'm not the only who considers this… problematic:

* [[…] it's so secure that it gets in the way of things which should appear to work.](http://lkml.iu.edu/hypermail/linux/kernel/0503.1/2540.html)
* [[RFC] Capabilities still can't be inherited by normal programs](http://www.gossamer-threads.com/lists/engine?do=post_view_flat;post=1641892;page=1;sb=post_latest_reply;so=ASC;mh=25;list=linux)


My main problem with the current design is that
**OpenWrt does not support file-based capabilities out of the box**.
Sure, it's compiled into the kernel, but the default file systems are compiled
without extended attributes which are in turn required to actually store the file-base capabilities.
Since I intended to use the hardened version of Wifidog on OpenWrt, this is a problem for me.
The obvious solution is to turn on extended attributes in my personal OpenWrt
builds, but that does not help anyone who runs stock images. In short, it must work out of the box.

## Workarounds and Drawbacks ##

Linux capabilities supports a compatibility mode. If a program is executed as UID0, all capabilities
are granted by default. My approach is now changed to **temporarily** switch to a non-privileged user
which still has **CAP\_NET\_ADMIN** and **CAP\_NET\_RAW**. Before executing *iptables*, Wifidog temporarily
switches back to UID 0 to reap the benefits of the compability mode. The subprocess is then automatically
granted all **INHERITABLE** and **PERMITTED** capabilities in **file**-based sets.

From the man page, I am still not quite sure why iptables works in this setup. The **EFFECTIVE** bit should
still be required, but it's only granted on SUID root executables.

This method has an important drawback. In my original design, I switched to a non-privileged user
using *setuid* which drops root completely. Now I need to use *seteuid* to set the effective
user ID only. This permits me to switch back to UID 0 to invoke iptables. The problem is that
an attacker, given an exploit for arbitrary code execution, could perform the same *seteuid* call.
This opens up the way for privilege escalation attacks as described earlier with */etc/crond.d*.

[Linux Security Modules](https://en.wikipedia.org/wiki/Linux_Security_Modules) like [SELinux](https://en.wikipedia.org/wiki/Security-Enhanced_Linux)
could provide a way out to restrict the files that wifidog (or an attacker) could access. The better
option here would be to enable extended attributes in OpenWrt, as that is far less intrusive and complex.

## The way forward ##

My patches will [hopefully land in Wifidog soon](https://github.com/wifidog/wifidog-gateway/pull/185).
As described above, the current security improvement are not as big as I had originally hoped. In particular,
privilege escalation is still too easy if code can be ran as UID 0 even a reduced set of capabilities.

For this reason, I would recommend running the capability-enabled Wifidog in a chroot environment. The
upcoming OpenWrt release will feature [jail support in its own init system, procd](http://thread.gmane.org/gmane.comp.embedded.openwrt.devel/31141/focus=31157).
I plan on updating the OpenWrt package to make use of this new feature. Even without seccomp support,
a traditional chroot would (hopefully) suffice to protect against the type of attacks
described above. Wifidog does not have **CAP\_CHROOT** which would be necessary to
[break out of chroot](http://www.bpfh.net/simes/computing/chroot-break.html).

## Thoughts ##

This was a fun learning experience. Wifidog is a bit more robust and secure, and that's what counts.

### Further Reading (summary from previous links) ###

* [Linux capabilities man page](http://linux.die.net/man/7/capabilities)
* [Chris Friedhoff on capabilities](https://friedhoff.org/posixfilecaps.html)
* [Finnbarr P. Murphy on capabilities](http://blog.fpmurphy.com/2009/05/linux-security-capabilities.html)
* [LKML discussion on capability inheritance](http://www.gossamer-threads.com/lists/engine?do=post_view_flat;post=1641892;page=1;sb=post_latest_reply;so=ASC;mh=25;list=linux)
* [Wifidog Pull request -- see src/capabilities.c](https://github.com/wifidog/wifidog-gateway/pull/185)


## Commented example code ##

First, here is the function that drops all but the required capabilities. Feel
free to bring your own implementation of **set\_user\_group**.

Call this early during initialization:

```C
void
drop_privileges(const char *user, const char *group)
{
    const int num_caps = 2;
    /* The capabilities we want. */
    cap_value_t cap_values[] = { CAP_NET_RAW, CAP_NET_ADMIN };
    cap_t caps;
    int ret = 0;
    /*
    * We are about to drop our effective UID to a non-privileged user.
    * This clears the EFFECTIVE capabilities set, so we later re-enable
    * these. We can do that because these are not cleared from
    * the PERMITTED set on seteuid().
    */
    set_user_group(user, group);
    caps = cap_get_proc();
    if (NULL == caps) {
        exit(1);
    }
    /* Clear all caps and then set the caps we desire */
    cap_clear(caps);
    cap_set_flag(caps, CAP_PERMITTED, num_caps, cap_values, CAP_SET);
    ret = cap_set_proc(caps);
    if (ret == -1) {
        exit(1);
    }
    cap_free(caps);
    caps = cap_get_proc();
    /* Now, we are running as non-privileged user and no capabilities are EFFECTIVE.
     * We need to regain capabilities by promoting them from PERMITTED to
     * EFFECTIVE and INHERITABLE.
     */
    cap_set_flag(caps, CAP_EFFECTIVE, num_caps, cap_values, CAP_SET);
    cap_set_flag(caps, CAP_INHERITABLE, num_caps, cap_values, CAP_SET);
    ret = cap_set_proc(caps);
    if (ret == -1) {
        printf("Could not set capabilities!\n");
        exit(1);
    }
    caps = cap_get_proc();
    if (NULL == caps) {
        printf("cap_get_proc failed, exiting!\n");
        exit(1);
    }
    printf("Final capabilities: %s", cap_to_text(caps, NULL));
    cap_free(caps);
}
```

Now, if you need to temporarily go back to UID 0 to execute
a subprocess, you might use something like this:

```C
/**
* Calls popen with root privileges.
*
* This method is a wrapper around popen(). The effective
* user and group IDs of the current process are temporarily set
* to 0 (root) and then reset to the original, typically non-privileged,
* values before returning.
*
* @param command First popen parameter
* @param type Second popen parameter
* @returns File handle pointer returned by popen
*/
FILE *
popen_as_root(const char *command, const char *type)
{
    FILE *p = NULL;
    uid_t uid = getuid();
    gid_t gid = getgid();
    switch_to_root();
    p = popen(command, type);
    set_uid_gid(uid, gid);
    return p;
}
```

For more details, see the full implementation in Wifidog
in *src/capabilities.c*.

