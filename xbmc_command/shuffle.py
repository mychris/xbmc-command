# -*- coding: utf-8 -*-

import sys

from . import core

class Command(core.Command):

    def call(self, args):
        mode = 'toggle'
        if args.state == 'y' or args.state == 'yes':
            mode = True
        elif args.state == 'n' or args.state == 'no':
            mode = False

        player = self.get_active_player_id()
        self.xbmc.Player.SetShuffle({
            'playerid': player,
            'shuffle': mode
        })

        self.xbmc.Player.GetProperties({
            'playerid': player,
            'properties': ['shuffled']
        })
        result = self.xbmc.recv('Player.GetProperties')

        if result['result']['shuffled']:
            result = 'Player shuffled'
        else:
            result = 'Player unshuffled'
        sys.stdout.write('%s\n' % result)

    def create_parser(self, parser):
        parser.prog = '%s repeat' % core.PROG
        parser.description = 'Shuffle/Unshuffle items in the player.'

        parser.add_argument('state', metavar='<state>', nargs='?',
                            choices=['yes', 'y', 'no', 'n', 'toggle', 't'],
                            default='toggle',
                            help="the shuffle state. Either 'yes', 'no' \
                                  or 'toggle', default toggle")

    @property
    def short_description(self):
        return 'Set the player shuffle mode'

# vim: ft=python ts=8 sts=4 sw=4 et:
