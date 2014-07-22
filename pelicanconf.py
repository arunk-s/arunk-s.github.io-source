#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Arun'
SITENAME = u'My crossroads and encounters'
SITEURL = 'http://arunk-s.github.io'

PATH = 'content'
USE_FOLDER_AS_CATEGORY = True

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'
THEME = '/home/arun/Work/blog/pelican-themes/pure-single'
COVER_IMG_URL = 'http://i.imgur.com/jGxiPTB.jpg'

#COVER_IMG_URL = 'http://i.imgur.com/nPLEHnN.jpg'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (
		('facebook', 'http://www.facebook.com/arun.sori/'),
		('github','http://www.github.com/arunk-s/'),
		)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
