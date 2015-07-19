#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Guillem Palou'
SITENAME = u'DS Vision'
SITEURL = ''

PATH = 'content'

# open the about_me file and read it
with open('additional_content/about_me.html') as f:
    about_me = f.read()

ABOUT_ME = about_me

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MARKUP = ('md')

PLUGIN_PATHS = ['/usr/local/anaconda/lib/python2.7/site-packages/pelican/pelican-plugins']
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook']

EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')


# Theme configuration
THEME = "pelican-bootstrap3"
BOOTSTRAP_THEME = 'yeti'
BOOTSTRAP_NAVBAR_INVERSE = True
BANNER='images/banner.png'

DISPLAY_TAGS_ON_SIDEBAR=False

# Blogroll

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/guillempalou'),
          ('linkedin', 'http://www.linkedin.com/in/guillempalou'),
          ('github', 'http://github.com/dsvision'),
          ('github', 'http://github.com/guillempalou'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
