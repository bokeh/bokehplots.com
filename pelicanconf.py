#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Bokeh contributors'
SITENAME = 'Bokeh'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

THEME = 'theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

IGNORE_FILES = ['*.scss', '*.css.map']

# Nav Links
NAV = (
    ('About', '/pages/about-bokeh.html'),
    ('Gallery', '//bokeh.pydata.org/en/latest/docs/gallery.html'),
    ('Docs', '//bokeh.pydata.org/en/latest/'),
    ('Github', '//github.com/bokeh/bokeh'),
)
NAV_SECOND = (
    ('Detailed user guide', '//bokeh.pydata.org/en/latest/docs/user_guide.html'),
    ('Tutorials in jupyter notebook', '//nbviewer.ipython.org/github/bokeh/bokeh-notebooks/blob/master/index.ipynb'),
    ('Hosting and installation', '//bokeh.pydata.org/en/latest/docs/installation.html'),
    ('FAQ', '/pages/faqs.html'),
)
# Community Links
LINKS = (
    ('FAQs', '/pages/faqs.html'),
    ('Technical vision', '/pages/technical-vision.html'),
    ('Roadmap', '/pages/roadmap.html'),
    ('Citation', '/pages/citation.html'),
)
# About Links
ABOUT = (
    ('About', '/pages/about-bokeh.html'),
    ('Team', '/pages/team.html'),
    ('Contact', '/pages/contact.html'),
)
# Social widget
SOCIAL = (
    ('Contribute', '/pages/contribute.html'),
    ('Mailing list', '//groups.google.com/a/anaconda.com/forum/#!forum/bokeh'),
    ('Gitter chat', '//gitter.im/bokeh/bokeh'),
    ('Github', '//github.com/bokeh/bokeh'),
    ('Twitter', '//twitter.com/BokehPlots'),
    ('YouTube', '//www.youtube.com/channel/UCK0rSk29mmg4UT4bIOvPYhw')
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
