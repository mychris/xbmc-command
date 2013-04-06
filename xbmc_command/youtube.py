# -*- coding: utf-8 -*-

import argparse
from . import core
try:
  import urlparse
except ImportError:
  import urllib.parse as urlparse

class Command(core.Command):

  def call(self, args):
    xbmc_file = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s'
    if args.id:
      xbmc_file = xbmc_file % args.id
    else:
      url = urlparse.urlparse(args.url)
      url_query = urlparse.parse_qs(url.query)
      if not 'v' in url_query:
        raise core.CommandException("No youtube video id found in given url.")
      xbmc_file = xbmc_file % url_query['v'][0]

    if args.quality:
      xbmc_file += '&quality=%s' % args.quality

    self.xbmc.Player.Open({'item': {'file': xbmc_file}})

  def create_parser(self, parser):
    parser.prog = '%s youtube' % core.prog
    parser.description = 'Open a youtube video file.'

    group= parser.add_mutually_exclusive_group(required=True)

    group.add_argument('--id', dest='id', metavar='<youtube id>',
        help='the youtube video id')

    group.add_argument('--url', dest='url', metavar='<url>',
        help='the youtube video url')

    parser.add_argument('--quality', dest='quality', default=None,
        choices=['1080p', '720p', 'low'],
        help='the quality to use. By default, no quality information will be \
            send and the plugin will choose one.')

  @property
  def short_description(self):
    return 'Play a youtube video'

# vim: ft=python ts=2 sts=2 sw=2 et:
