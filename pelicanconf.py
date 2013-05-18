#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Michael Haas'
SITENAME = u'Michael Haas'
SITEURL = ''

DISPLAY_PAGES_ON_MENU = True

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'en'

# Blogroll

LINKS = None

# Social widget

#SOCIAL = None

SOCIAL = [  ("github", "http://github.com/mhaas/"),
            ("XING", "https://www.xing.com/profile/Michael_Haas135"),
            ("Google+", "https://plus.google.com/115592321379755190116/posts")
         ] 


GPLUS = "https://plus.google.com/115592321379755190116/posts"

GSITEVER = "TGefRjRcqUNOTWOFQwqb5C-0pMX6aoJq8cGWgZhwKeM"

DEFAULT_PAGINATION = 10

STATIC_PATHS = ([u'images',u'downloads'])

#THEME = "notmyidea"
#THEME = "simple"
THEME = "/home/laga/dev/pelican-themes/themes/notmyidea"

PLUGINS = ['pelican.plugins.assets']

DISPLAY_CATS_ON_MENU = False
