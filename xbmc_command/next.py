# -*- coding: utf-8 -*-

from . import core

class Command(core.Command):

    def call(self, args):
        player_id = self.get_active_player_id()
        if player_id < 0:
            return
        self.xbmc.Player.GoTo({'playerid': player_id, 'to': 'next'})

    def create_parser(self, parser):
        parser.prog = '%s next' % core.PROG
        parser.description = 'Play the next item in the playlist.'

    @property
    def short_description(self):
        return 'Go to the next item in the playlist'

# vim: ft=python ts=8 sts=4 sw=4 et:
