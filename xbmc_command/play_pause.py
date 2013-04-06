# -*- coding: utf-8 -*-

from . import core

class Command(core.Command):

  def call(self, args):
    player_id = self.get_active_player_id()
    if player_id < 0:
      return

    self.xbmc.Player.PlayPause({'playerid': player_id})

  def create_parser(self, parser):
    parser.prog = '%s play_pause' % core.prog
    parser.description = 'Toggle play/pause.'

  @property
  def short_description(self):
    return 'Toggle play/pause'

# vim: ft=python ts=2 sts=2 sw=2 et:
