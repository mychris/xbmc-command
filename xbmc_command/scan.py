# -*- coding: utf-8 -*-

import argparse
from . import core

class Command(core.Command):

  def call(self, args):
    if args.audio:
      self.xbmc.AudioLibrary.Scan({'directory':args.directory})
    elif args.video:
      self.xbmc.VideoLibrary.Scan({'directory':args.directory})

  def create_parser(self, parser):
    parser.prog = '%s scan' % core.prog
    parser.description = 'Scans the XBMC audio or video sources for new library items.'

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('--audio', dest='audio', action='store_true',
        default=False,
        help='scans the audio sources for new library items')

    group.add_argument('--video', dest='video', action='store_true',
        default=False,
        help='scans the video sources for new library items')

    parser.add_argument('--dir', dest='directory', metavar='<directory>',
        default='',
        help='the directory to scan, default \'\'')

    return parser

  @property
  def short_description(self):
    return 'Scans the XBMC library'

# vim: ft=python ts=2 sts=2 sw=2 et:
