Title: Automated Load Testing for Wifidog
Date: 2015-04-01
lang: en
tags: wifidogs, oss

## Wifidog and the dreaded memory leaks ##

I've recently made quite a few contributions to the
[wifidog project](http://dev.wifidog.org/). It has
been a lot of fun to see the project coming back to life after being almost
dormant for the last couple of years. Now the bug tracker on Github is fuller
than ever and the pull requests keep coming.

Some people reported memory leaks, particularly on busy access points
([#34](https://github.com/wifidog/wifidog-gateway/issues/34),
[#55](https://github.com/wifidog/wifidog-gateway/issues/55#issuecomment-85004888)).
Debugging these problems. is a bit problematic. None of the developers
have a suitable high-usage wifidog instance available. Additionally,
typical tools like [valgrind's memcheck](http://valgrind.org/info/tools.html)
or the GCC/Clang address sanitizer are not available on your typical
OpenWRT device. Heck, my last device only had 4MB flash and I had
to disable IPV6 support to fit everything.


## The magic of virtual network interfaces ##

Wifidog internally uses the MAC and IP addresses to identify a client.
To simulate clients which log in, log out or
[send random stuff](https://en.wikipedia.org/wiki/Fuzzing), it is not
enough to add another IP address on a virtual interface. Fortunately,
there is
[**macvlan**](http://backreference.org/2014/03/20/some-notes-on-macvlanmacvtap/),
a special device type which provides a virtual layer2 interface.

Once I had created a good amount of virtual interfaces for the clients
and an additional one for Wifidog, I only needed a mock 
[authentication server](http://dev.wifidog.org/wiki/doc/developer/FlowDiagram)
and a client script which talks HTTP to Wifidog.
For the auth server, I wrote a very simple python script which randomly
answers **AUTH\_DENIED** or **AUTH\_ALLOWED**.

The client script first requests a random website,
thus triggering the redirect code in Wifidog. The second request is a log-in
request. With a 33% chance, a subsequent logout is triggered. The fun part
here is provided by the [multiprocessing](https://docs.python.org/2/library/multiprocessing.html)
package. The 40 or so virtual clients are distributed among three parallel
processes. This ensures some randomness in request order and should also
exercise the threading code in Wifidog.

There was one pitfall when implementing the client script. Although I do have
virtual interfaces with (real) IP addresses, I needed to tell Python
to use these as the source address for the HTTP requests. This is not exactly
straightforward and some proposals include
[monkey-patching the socket code.](http://stackoverflow.com/a/1150423/4306056).
Python 2.7 however introduced a **source** parameter to HTTPConnection. It is
not directly exposed in **urllib2**, so I decided to use the lower-level
**httplib.HTTPConnection** interface ([source](http://stackoverflow.com/a/19548555/4306056)):

    source = "10.0.10.5"
    conn = HTTPConnection(target, PORT, timeout=10, source_address=(source, 0))
    conn.connect()
    token = str(uuid.uuid4())
    conn.request("GET", "/wifidog/auth?token=" + token )
    try:
        resp = conn.getresponse()
        # this causes wifidog to ask our mock auth server if the token is
        # correct
        resp.read()
    except Exception as e:
        # basic error handling...
        print e

One last problem arises even though I did everything right [tm]. If both
the mock clients and Wifidog run on the same machine, the MAC addresses will
not show up in the ARP table. To work around this, I added a way to pass
a mock ARP table in the same format as **/proc/net/arp** to wifidog with
the **-a** switch. Now it works on localhost and over the network.

## Cool story, bro. Does it help? ##

In fact, the load tester slash pseudo-fuzzing script helped uncover some defects:

* [Missing error recovery in HTTP server](https://github.com/wifidog/wifidog-gateway/pull/173)
* [Prevent possible leaks](https://github.com/wifidog/wifidog-gateway/pull/169)
* [Invalid memory access due to race condition](https://github.com/wifidog/wifidog-gateway/pull/168)

Granted, the last issue was known beforehand, but the script provided a rather
reliable way to trigger it.

Most importantly, we can monitor if we're still suffering from memory leaks. And indeed we do:

![Wifidog memory usage](|filename|/images/wifidog_memory_usage.png)

This is the current situation.
These leaks are a bit harder to catch as valgrind shows no lost memory. There likely
is memory allocated (and still referenced) without being free'd. Valgrind has a
**-show-reachable=yes** switch which is useful in this scenario.

## Other fun code quality tool ##

Beyond automatically hammering Wifidog with requests, we have some more fun toys.
Wifidog now uses [https://travis-ci.org/wifidog/wifidog-gateway](Travis CI) to
automatically build new code with both Clang and GCC with
**-Werror -Wall -Wextra** which should make the code base a bit more resilient.
We have already fixed all compiler warnings.
Beyond compile-time checks, Coverity provides their [static analyzer free of charge
for open source projects](https://scan.coverity.com/projects/4595).
Integrated with Github and Travis-CI, it is extremely
easy to find and fix defects ([#165](https://github.com/wifidog/wifidog-gateway/pull/165),
([#163](https://github.com/wifidog/wifidog-gateway/pull/160),
([#160](https://github.com/wifidog/wifidog-gateway/pull/160)…).
We have also tried the free clang-analyzer which, while helpful,
did not catch as many defects as the non-free (as in speech) coverity scan.

