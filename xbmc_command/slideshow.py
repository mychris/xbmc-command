# -*- coding: utf-8 -*-

import argparse
from . import core

class Command(core.Command):

  def call(self, args):
    self.xbmc.Player.Open({'item':{'path':args.directory, 'recursive':True}})

  def create_parser(self, parser):
    parser.prog = '%s slideshow' % core.prog
    parser.description = 'Starts a recursive slideshow of the specified Picture directory.'

    parser.add_argument('--dir', dest='directory', metavar='<directory>',
        default='', help='the Picture directory, default \'\'')

    return parser

  @property
  def short_description(self):
    return 'Starts a Picture slideshow'

# vim: ft=python ts=2 sts=2 sw=2 et:
