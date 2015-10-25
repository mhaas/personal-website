Title: Stunnel 5.14 in OpenWRT Chaos Calmer
Date: 2015-04-07
lang: en
tags: stunnel, oss

## Stunnel 5.14 Update ##

Somewhere along the way, I became the new maintainer for the [stunnel](https://www.stunnel.org/index.html)
package [in OpenWRT](https://github.com/openwrt/packages/tree/master/net/stunnel).

I had initially needed stunnel because my auth server for wifidog only speaks
TLS. In my testing, I required a more version of stunnel (for some reason I forgot).

At that point, the stunnel package had been abandoned already and was only available
in OpenWrt 14.07 as part of the **oldpackages** repository. I had already built
a working packaging script for stunnel 5.10
[based on another attempt](https://sites.google.com/site/twisteroidambassador/openwrt/stunnel).
So I figured, why not submit it to the OpenWrt repository?

Since then, an automatic email (nice!) reminded me that stunnel 5.14 had been released, including
[some security fixes](https://www.stunnel.org/sdf_ChangeLog.html). Luckily, the patches required
for OpenWrt [still applied cleanly](https://github.com/openwrt/packages/tree/master/net/stunnel/patches).


Some items remain on the TODO list:

* Make SSP configurable upstream so I don't have to maintain *011\_disable\_ssp\_linking.patch*
* Failing that, make sure SSP works if enabled in OpenWrt buildroot
* Get rid of *010\_fix\_getnameinfo.patch*

Overall, I'm quite happy with the packaging. Compared to earlier versions, only two trivial patches
are required and the dependency on **libpthread** was dropped.

Wifidog speaks [TLS natively](https://github.com/wifidog/wifidog-gateway/pull/63) these days. I
personally don't need stunnel right now, but it's always good to have more cryptography
options in a post-snowden world.



