#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Michael Haas'
SITENAME = u'Michael Haas'
SITEURL = 'https://computerlinguist.org'

DISPLAY_PAGES_ON_MENU = True

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'en'

MARKUP = ('md', )

# Blogroll

LINKS = None

# Social widget

#SOCIAL = None


GPLUS = "https://plus.google.com/115592321379755190116/posts"

SOCIAL = [("github", "http://github.com/mhaas/"),
          ("XING", "https://www.xing.com/profile/Michael_Haas135"),
          ("Linkedin", "https://www.linkedin.com/in/haasm"),
          ("Stack Overflow",
           "https://stackoverflow.com/users/4306056/michael-haas")]

GSITEVER = "y5JSK6qi6Lx8IIL6v0ClQ4hGgVLpkbpwN4PogB5ay98"

FAVPNG = u"static/images/MH.png"

# FAVICO = u"blah"
DEFAULT_PAGINATION = 10

STATIC_PATHS = ([u'images', u'downloads', u'pages/ma-thesis'])

#THEME = "notmyidea"
THEME = "/home/mhaas/dev/pelican-themes/themes/notmyidea"

PLUGIN_PATHS = ['/home/mhaas/dev/pelican-plugins']
PLUGINS = ['assets', 'sitemap', 'optimize_images']  # 'w3c_validate']

SITEMAP = {'format': 'xml'}

INDEX_SAVE_AS = 'blog_index.html'

MENUITEMS = [('Blog', SITEURL + '/' + INDEX_SAVE_AS)]

DISPLAY_CATS_ON_MENU = False
