#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

import xbmc_command

setup(
  name = xbmc_command.core.prog,
  version = xbmc_command.core.version,
  description = 'Simple xbmc-command client',
  author = 'Christoph Göttschkes',
  author_email = 'just.mychris@googlemail.com',
  url = 'https://github.com/mychris/xbmc-command',
  download_url = 'https://github.com/mychris/xbmc-command/tarball/master',
  scripts = ['xbmc-command'],
  packages = ['xbmc_command'],
  classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Operating System :: Unix',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'
  ],
  license = 'GPL v3 or later',
  data_files = [('share/doc/xbmc-command', ['README.md', 'LICENSE'])]
)

# vim: ft=python ts=2 sts=2 sw=2 et:
