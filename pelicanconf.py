#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Darrick Sturgeon'
SITENAME = 'S Vision'
SITEURL = ''
SITELOGO = SITEURL + '/images/profile.jpg'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('About Me', 'about-me.html'),
        ('Imaging', 'category/imaging.html'),
        ('My Github', 'https://github.com/dasturge'),
        ('DCAN-labs Github', 'https://github.com/DCAN-Labs'),
        ('Python.org', 'http://python.org/'))

# social widget
social = (('github', 'https://github.com/dasturge'),
          ('another link', '#'))

DEFAULT_PAGINATION = 10

OUTPUT_RETENTION = ['.git']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

IGNORE_FILES = [".ipynb_checkpoints"]

THEME = "/home/euler/pelican-themes/Flex"

