# -*- coding: utf-8 -*-

from . import core
try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse

class Command(core.Command):

    def call(self, args):
        xbmc_file = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s'
        try:
            url = urlparse.urlparse(args.link)
            url_query = urlparse.parse_qs(url.query)
            if 'v' not in url_query:
                raise core.CommandException("No youtube video id found in given url.")
            xbmc_file = xbmc_file % url_query['v'][0]
        except ValueError:
            xbmc_file = xbmc_file % args.link

        if args.quality:
            xbmc_file += '&quality=%s' % args.quality

        self.xbmc.Player.Open({'item': {'file': xbmc_file}})

    def create_parser(self, parser):
        parser.prog = '%s youtube' % core.PROG
        parser.description = 'Open a youtube video file.'

        parser.add_argument('link', metavar='<link>',
                            help='the url or the youtube video id')

        parser.add_argument('--quality', dest='quality', default=None,
                            choices=['1080p', '720p', 'low'],
                            help='the quality to use. \
                                  By default, no quality information will be \
                                  send and the XBMC plugin will choose one.')

    @property
    def short_description(self):
        return 'Play a youtube video'

# vim: ft=python ts=8 sts=4 sw=4 et:
