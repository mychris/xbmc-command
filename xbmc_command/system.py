# -*- coding: utf-8 -*-

import argparse
from . import core

class Command(core.Command):

  def call(self, args):
    if args.quit:
      self.xbmc.Application.Quit()
    elif args.shutdown:
      self.xbmc.System.Shutdown()
    elif args.reboot:
      self.xbmc.System.Reboot()
    elif args.suspend:
      self.xbmc.System.Suspend()
    elif args.hibernate:
      self.xbmc.System.Hibernate()

  def create_parser(self, parser):
    parser.prog = '%s system' % core.prog
    parser.description = 'Handle the XBMC system.'

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('--quit', dest='quit', action='store_true',
        default=False, help='Quit XBMC')

    group.add_argument('--shutdown', dest='shutdown', action='store_true',
        default=False, help='Shuts the system running XBMC down')

    group.add_argument('--reboot', dest='reboot', action='store_true',
        default=False, help='Reboots the system running XBMC')

    group.add_argument('--suspend', dest='suspend', action='store_true',
        default=False, help='Suspends the system running XBMC')

    group.add_argument('--hibernate', dest='hibernate', action='store_true',
        default=False, help='Puts the system running XBMC into hibernate mode')

  @property
  def short_description(self):
    return 'Call system procedure'

# vim: ft=python ts=2 sts=2 sw=2 et:
