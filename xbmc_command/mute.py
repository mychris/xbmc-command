# -*- coding: utf-8 -*-

from . import core

class Command(core.Command):

  def call(self, args):
    self.xbmc.Application.SetMute({'mute': 'toggle'})

  def create_parser(self, parser):
    parser.prog = '%s mute' % core.prog
    parser.description = 'Toogle mute/unmute.'

  @property
  def short_description(self):
    return 'Toggle mute'

# vim: ft=python ts=2 sts=2 sw=2 et:
