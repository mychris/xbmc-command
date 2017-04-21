# -*- coding: utf-8 -*-

from . import core

class Command(core.Command):

    def call(self, args):
        if not args.stop:
            self.xbmc.Player.Open({
                'item': {
                    'path': args.directory,
                    'recursive': True
                }
            })
            return

        self.xbmc.Player.GetActivePlayers()
        players = self.xbmc.recv('Player.GetActivePlayers')
        if not 'result' in players:
            return

        for player in players['result']:
            if player['type'] == 'picture':
                self.xbmc.Player.Stop({'playerid': player['playerid']})

    def create_parser(self, parser):
        parser.prog = '%s slideshow' % core.PROG
        parser.description = 'Starts (or stops) a recursive slideshow of the \
                              specified Picture directory.'

        parser.add_argument('--dir', dest='directory', metavar='<directory>',
                            default='',
                            help="the Picture directory, default ''")

        parser.add_argument('--stop', dest='stop', action='store_true',
                            default=False,
                            help='stop current slideshow (if present)')

        return parser

    @property
    def short_description(self):
        return 'Starts a Picture slideshow'

# vim: ft=python ts=8 sts=4 sw=4 et:
