#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Michael Haas'
SITENAME = u'Michael Haas'
SITEURL = 'http://www.computerlinguist.org/'

DISPLAY_PAGES_ON_MENU = True

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'en'

# Blogroll

LINKS = None

# Social widget

#SOCIAL = None

SOCIAL = [  ("github", "http://github.com/mhaas/"),
            ("XING", "https://www.xing.com/profile/Michael_Haas135"),
            ("Google+", "https://plus.google.com/115592321379755190116/posts"),
           ("Stack Overflow", "https://stackoverflow.com/users/4306056/michael-haas")]


GPLUS = "https://plus.google.com/115592321379755190116/posts"

GSITEVER = "TGefRjRcqUNOTWOFQwqb5C-0pMX6aoJq8cGWgZhwKeM"

FAVPNG = u"static/images/MH.png"

# FAVICO = u"blah"
DEFAULT_PAGINATION = 10

STATIC_PATHS = ([u'images', u'downloads', u'pages/ma-thesis'])

#THEME = "notmyidea"
#THEME = "simple"
THEME = "/home/laga/dev/pelican-themes/themes/notmyidea"

PLUGINS = ['pelican.plugins.assets']

DISPLAY_CATS_ON_MENU = False
