# -*- coding: utf-8 -*-
# https://kodi.tv/addon/plugins-video-add-ons/twitch
# https://github.com/MrSprigster/Twitch-on-Kodi

import argparse
from . import core
try:
  import urlparse
except ImportError:
  import urllib.parse as urlparse

class Command(core.Command):

  def call(self, args):
    uri_template = 'plugin://plugin.video.twitch/playLive/%s/%s'

    quality = self.quality_to_ident(args.quality) if args.quality else 0

    channel = args.link
    url = urlparse.urlparse(args.link)
    if not url.path:
      raise core.CommandException("No channel provided")
    channel = url.path.strip()
    if url.scheme and channel:
      channel = channel[1:]
    if not channel:
      raise core.CommandException("Unable to parse channel")

    uri = uri_template % (channel, quality)
    self.xbmc.Player.Open({'item': {'file': uri}})

  def quality_to_ident(self, quality):
    mapping = {
        'source': 0,
        '1080p60': 1,
        '1080p30': 2,
        '720p60': 3,
        '720p30': 4,
        '540p30': 5,
        '480p30': 6,
        '360p30': 7,
        '240p30': 8,
        '144p30': 9,
        'dialog': -1,
    }
    ret = mapping.get(quality)
    if ret != None:
      return ret
    raise core.CommandException("Unknow quality '%s'" % quality)

  def create_parser(self, parser):
    parser.prog = '%s twitch' % core.prog
    parser.description = '''Open a twitch channel.
This command requires the twitch plugin to be installed.'''

    parser.add_argument('link', metavar='<link>',
        help='the url or name of the twitch channel')

    parser.add_argument('--quality', dest='quality', default=None,
        choices=['1080p60', '1080p30', '720p60', '720p30', 'dialog'],
        help='the quality to use. By default, the source quality of the \
            channel will be used.')

  @property
  def short_description(self):
    return 'Play a twitch channel'

# vim: ft=python ts=2 sts=2 sw=2 et:
