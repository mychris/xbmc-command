# -*- coding: utf-8 -*-

from . import core

class Command(core.Command):

  def call(self, args):
    player_id = self.get_active_player_id()
    if player_id < 0:
      return

    self.xbmc.Player.GoTo({'playerid':player_id, 'to': 'previous'})

  def create_parser(self, parser):
    parser.prog = '%s prev' % core.prog
    parser.description = 'Play the previous item in the playlist.'

  @property
  def short_description(self):
    return 'Go to the previous item in the playlist'

# vim: ft=python ts=2 sts=2 sw=2 et:
