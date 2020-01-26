# -*- coding: utf-8 -*-

from . import core

class Command(core.Command):

    def call(self, args):
        player_id = self.get_active_player_id()
        if player_id < 0:
            raise core.CommandException('No active player found')

        self.xbmc.Player.PlayPause({'playerid': player_id, 'play': 'toggle'})
        result = self.xbmc.recv('Player.PlayPause')
        if 'error' in result:
            raise core.CommandException(result['error']['message'])

    def create_parser(self, parser):
        parser.prog = '%s play-pause' % core.PROG
        parser.description = 'Toggle play/pause.'

    @property
    def short_description(self):
        return 'Toggle play/pause'

# vim: ft=python ts=8 sts=4 sw=4 et:
