# -*- coding: utf-8 -*-

import sys
from . import core

class Command(core.Command):

  def call(self, args):
    player = self.get_active_player_id()
    self.xbmc.Player.SetRepeat({'playerid': player, 'repeat': args.state})

    self.xbmc.Player.GetProperties({'playerid': player, 'properties':['repeat']})
    result = self.xbmc.recv('Player.GetProperties')

    sys.stdout.write('Repeat: %s\n' % result['result']['repeat'])

  def create_parser(self, parser):
    parser.prog = '%s repeat' % core.prog
    parser.description = 'Set the repeat state to off, one, all or cycle it.'

    parser.add_argument('state', metavar='<state>', nargs='?',
        choices=['off', 'one', 'all', 'cycle'], default='cycle',
        help='the mute state. Either \'off\', \'one\', \'all\',  or \'cycle\', default cycle')

  @property
  def short_description(self):
    return 'Set the repeat state'

# vim: ft=python ts=2 sts=2 sw=2 et:
