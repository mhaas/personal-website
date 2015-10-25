Title: Wifidog 1.2.1 released!
Date: 2015-04-17
lang: en
tags: wifidogs, oss


We released [version 1.2.1 of the Wifidog gateway](https://github.com/wifidog/wifidog-gateway/releases/tag/1.2.1)
yesterday. I'm extremely happy with this release. We put in lots of polishing and fixed a lot of bugs.


Here's the changelog:

* Fix build (#127, #128)
* Integrate with Travis CI
* Integrate with Coverity Scan
* Fix several memory leaks and other potential problems uncovered by static analysis
* Refactor SSL initialization
* Fix a truncation issue around 112 clients in the status page. (#47)
* Prevent duplicate TrustedMAC entries (#145)
* Enhance safe_malloc to always zero memory (#155)
* Fix segfault related pstr_t's buffer (#149)
* Add open the firewall if no auth servers can be reached (optional, #90)
* Add configurable ARP table location (-a switch). Useful for mock ARP tables during load tests (#166)
* Various other fixes and minor improvements, see [1.2.0...1.2.1](https://github.com/wifidog/wifidog-gateway/compare/1.2.0...1.2.1)

Note that [capabilities]({filename}hardening_wifidog_with_linux_capabilities.md) is not in this release yet.
Next stop: getting Wifidog back into OpenWRT.

