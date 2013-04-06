# -*- coding: utf-8 -*-

import argparse
from . import core

try:
  import urllib
except ImportError:
  import urllib.parse as urllib

class Command(core.Command):
  """ NOT TESTED, need subscription? """

  def call(self, args):
    xbmc_file = 'plugin://plugin.audio.lastfm/?%s&mode=%s'

    url = None
    mode = None

    if args.tag:
      mode = 'tags'
      url = args.tag
    elif args.artist:
      mode = 'artists'
      url = args.url

    url = urllib.urlencode({'url': url})

    xbmc_file = xbmc_file % (url, mode)
    self.xbmc.Player.Open({'item': {'file': xbmc_file}})

  def create_parser(self, parser):
    parser.prog = '%s lastfm' % core.prog
    parser.description = 'Play music from last.fm.'

    group= parser.add_mutually_exclusive_group(required=True)

    group.add_argument('--tag', dest='tag', metavar='<tag>',
        help='the tag to play')

    group.add_argument('--artist', dest='artist', metavar='<artist>',
        help='the artist to play')

  @property
  def short_description(self):
    return 'Play music from last.fm'

# vim: ft=python ts=2 sts=2 sw=2 et:
