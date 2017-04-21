# -*- coding: utf-8 -*-

from . import core

class Command(core.Command):

    def call(self, args):
        player_id = self.get_active_player_id()
        if player_id < 0:
            return

        self.xbmc.Player.PlayPause({'playerid': player_id})

    def create_parser(self, parser):
        parser.prog = '%s play-pause' % core.PROG
        parser.description = 'Toggle play/pause.'

    @property
    def short_description(self):
        return 'Toggle play/pause'

# vim: ft=python ts=8 sts=4 sw=4 et:
