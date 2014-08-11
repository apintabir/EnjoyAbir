#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Abir Majumdar'
SITENAME = 'Abir Majumdar'
SITETAGLINE = 'demonstrably incompetent'
SITEURL = 'http://enjoyabir.com'
DEFAULT_CATEGORY = 'misc'

TIMEZONE = 'America/Chicago'
DEFAULT_DATE_FORMAT = ('%Y-%m-%d')
DEFAULT_LANG = 'en'

DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
	('Home', '/index.html'),
	('About', '/pages/about.html'),
	('Archives', '/archives.html'),
)

STATIC_PATHS = [
	'images',
	'swf',
	'extras'
]

THEME = './theme/EnjoyAbir'



# Blogroll
#LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
#          ('Python.org', 'http://python.org'),
#          ('Jinja2', 'http://jinja.pocoo.org'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 3
