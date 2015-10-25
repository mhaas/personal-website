Title: Wifidog 1.3.0 released!
Date: 2015-10-25
lang: en
tags: wifidogs, oss

We released [version 1.3.0 of the Wifidog gateway](https://github.com/wifidog/wifidog-gateway/releases/tag/1.3.0)
yesterday.

Here's the changelog:

* Add delta traffic stats (#211)
* Add config options for popular servers (#78, #203)
* Add SNI support for SSL (#226)
* Add option to save pid file (#217)
* Fix build with MUSL (#221)
* Fix wolfSSL detection for --enable-cyassl configure option (#224)

We still have some outstanding pull requests which we will hopefully process for release
1.4.0.

Note that [capabilities]({filename}hardening_wifidog_with_linux_capabilities.md) is still not in this release.
I'm going to submit an update for the Wifidog OpenWrt package later today, once I have verified
the build with current OpenWrt master.

