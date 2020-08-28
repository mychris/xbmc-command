# -*- coding: utf-8 -*-
# https://kodi.tv/addon/plugins-video-add-ons/twitch
# https://github.com/MrSprigster/Twitch-on-Kodi

from . import core

try:
    import urllib.parse
except ImportError:
    import urllib.parse as urlparse

class Command(core.Command):

    def call(self, args):
        uri_template = 'plugin://plugin.video.twitch/?mode=play&channel_name=%s&quality=%s&ask=%s'

        ask = 'false'
        quality = 'Source'
        if args.quality in ('dialog', 'Dialog', 'ask'):
            ask = 'true'
        elif args.quality not in ('source', 'Source'):
            quality = args.quality

        channel = args.link
        url = urllib.parse.urlparse(args.link)
        if not url.path:
            raise core.CommandException("No channel provided")
        channel = url.path.strip()
        if url.scheme and channel:
            channel = channel[1:]
        if not channel:
            raise core.CommandException("Unable to parse channel")

        uri = uri_template % (channel, quality, ask)
        self.xbmc.Player.Open({'item': {'file': uri}})
        result = self.xbmc.recv('Player.Open')

    def create_parser(self, parser):
        parser.prog = '%s twitch' % core.PROG
        parser.description = 'Open a twitch channel. \
                              This command requires the twitch plugin \
                              to be installed.'

        parser.add_argument('link', metavar='<link>',
                            help='the url or name of the twitch channel')

        parser.add_argument('--quality', dest='quality', default='Source',
                            help='the quality to use. By default, the source \
                                  quality of the channel will be used. \
                                  Use "dialog" if you wish to select it while opening the stream.')

    @property
    def short_description(self):
        return 'Play a twitch channel'

# vim: ft=python ts=8 sts=4 sw=4 et:
