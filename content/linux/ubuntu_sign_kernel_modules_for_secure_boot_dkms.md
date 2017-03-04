Title: Make DKMS sign kernel modules for secure boot on Ubuntu 16.04
Date: 2017-03-03
lang: en
tags: ubuntu, secure-boot, oss, dkms

## Ubuntu, DKMS and Secure Boot ##

Starting with Ubuntu 16.04, the kernel will refuse to load unsigned
modules. This is pretty reasonable from a security point of view; a
chain of trust is established starting from a set of keys in the system
ROM. The kernel will refuse any unsigned modules or modules signed with
a key it can't verify via the chain of trust.

This is a bit unfortunate, however, for third-party modules which are not
signed with Canonical's key. When installing these third-party modules
such as VirtualBox or the NVidia driver, Ubuntu will thus prompt the user
to disable Secure Boot via the shim boot loader. In this scenario, the
UEFI firmware will load the trusted shim boot loader, which is signed by
Microsoft for Canonical. The shim loader has been configured to allow
unsigned code to execute, enabling third-party modules but also breaking the
chain of trust.

## Using your own keys ##

A better way is to make your own set of keys known to the system. You can then
sign modules or kernels with your own key and they will be executed once verify
. You may even go as far as distrusting the default microsoft keys.

The default way in Ubuntu is not to change Secure Boot in the BIOS, which
is not possible on some hardware. Instead, they provide the facility to
disable secure boot via the shim loader OR to enroll Machine Owner Keys
into the shim. This latter option is well documented, e.g. in this [answer on AskUbuntu](http://askubuntu.com/a/768310/661359).

## Automatic signing of DKMS kernel modules ##

This process is not automatic enough for my tastes. I don't want to
manually re-sign the .ko files on every kernel update - that's for people
with too much time on their hands. Instead, I added a `POST_BUILD` hook to
DKMS which will automatically sign the kernel modules for me.

This requires two parts. One generic DKMS config file, which we will need
to link to the desired DKMS module name.

Create a file `/etc/dkms/sign-kernel-objects.conf` with the following
content:

    POST_BUILD=../../../../../../root/sign-kernel.sh

Next, create the script which actually signs the modules in `/root/sign-kernel.sh`:

    #!/bin/bash

    cd ../$kernelver/$arch/module/

    for kernel_object in *ko; do
         echo "Signing kernel_object: $kernel_object"
        /usr/src/linux-headers-$kernelver/scripts/sign-file sha256 /root/MOK.priv /root/MOK.der "$kernel_object";
    done


Finally, activate the generic config for every module that you need.
Keep in mind that module here does not refer to the name of the .ko file,
but rather to the name used by DKMS for the entire package. Check the directory
names in `/var/lib/dkms/`.

To activate signing for virtualbox, execute:

    sudo ln -s /etc/dkms/sign-kernel-objects.conf /etc/dkms/virtualbox.conf

I did not immediately find a way to enable signing for all new modules without
manually creating that config override per module. It may be possible to hack
that together via `/etc/dkms/platform.conf`.

You may have noticed the liberal use of relative paths above. This is a bit
clumsy, of course. DKMS insists on executing the `POST_BUILD` scripts (and
other related hooks) as a relative path to the module directory.

This can be seen in the `run_build_script` function in my /usr/sbin/dkms:

    run_build_script() {
        # $1 = script type
        # $2 = script to run
        local script_type run
        [[ $2 ]] || return 0
        case "$1" in
            pre_build|post_build) script_type='build';;
            *) script_type='source'
        esac
        run="$dkms_tree/$module/$module_version/$script_type/$2"
        echo $run
        if [[ -x ${run%% *} ]]; then
            
            echo $""
            echo $"Running the $1 script:"
            (
                cd "$dkms_tree/$module/$module_version/$script_type/"
                exec $run
            )
        else
            echo $""
            warn $"The $1 script is not executable."
        fi
    }


## Is this secure? ##

Good question! I am not really qualified to answer that :)

A comment in the Ask Ubuntu Thread above raises the issue that leaving
an unencrypted MOK around will enable any attacker who has root privileges
to sign and insert malicious kernel modules. On the other hand, an
attacker with root privileges also can simply add their own MOK
IF they have physical/KVM access to the shim loader and if there is
no boot password set in the bios.

If the private key required a PIN, this would be less of an issue - but
also break the script outlined above, unless you got fancy and perhaps put
the key on an USB stick and only plug that in as needed.

There's lots of possible scenarios and outcomes. I do know that the process
above is good enough for me.
