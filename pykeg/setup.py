#!/usr/bin/env python
"""Kegbot kegerator controller software

This package contains Kegbot core controller and Django
frontend package.

Kegbot is a hardware and software system to record and monitor access to a beer
kegerator.  For more information and documentation, see http://kegbot.org/
"""

DOCLINES = __doc__.split('\n')

VERSION = '0.9.6'
SHORT_DESCRIPTION = DOCLINES[0]
LONG_DESCRIPTION = '\n'.join(DOCLINES[2:])
DEPENDENCIES = [
  'kegbot-pyutils >= 0.1.4',
  'kegbot-api >= 0.1.2',

  'django >= 1.3',
  'django-autoslug',
  'django-imagekit >= 2.0',
  'django-registration',
  'django-socialregistration >= 0.5.4',
  'django_extensions',

  'Celery',
  'django-celery',
  'django-kombu',

  'South >= 0.7.3',
  'django-crispy-forms',
  'django-icanhaz',
  'django_nose',
  'facebook-sdk >= 0.3.0',
  'foursquare',
  'gunicorn >= 0.16.1',
  'poster', # needed by foursquare
  'protobuf >= 2.4.1',
  'pylcdui >= 0.5.5',
  'python-gflags >= 1.8',
  'pytz',
  'requests', # needed by oauth
  'tweepy',
]

def setup_package():
  from distribute_setup import use_setuptools
  use_setuptools()
  from setuptools import setup, find_packages

  setup(
      name = 'kegbot',
      version = VERSION,
      description = SHORT_DESCRIPTION,
      long_description = LONG_DESCRIPTION,
      author = 'mike wakerly',
      author_email = 'opensource@hoho.com',
      url = 'http://kegbot.org/',
      packages = find_packages('src'),
      package_dir = {
        '' : 'src',
      },
      scripts = [
        'distribute_setup.py',
        'bin/kegbot-admin.py',
      ],
      install_requires = DEPENDENCIES,
      dependency_links = [
          'https://github.com/rem/python-protobuf/tarball/master#egg=protobuf-2.4.1',
      ],
      include_package_data = True,
      entry_points = {
        'console_scripts': ['instance=django.core.management:execute_manager'],
      },
  )

if __name__ == '__main__':
  setup_package()
