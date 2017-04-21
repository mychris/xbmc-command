# -*- coding: utf-8 -*-

from . import core

class Command(core.Command):

    def call(self, args):
        if args.state == 'yes' or args.state == 'y':
            args.state = True
        elif args.state == 'no' or args.state == 'n':
            args.state = False
        self.xbmc.Application.SetMute({'mute': args.state})

    def create_parser(self, parser):
        parser.prog = '%s mute' % core.PROG
        parser.description = 'Set the mute state to mute/unmute or toggle it.'

        parser.add_argument('state', metavar='<state>', nargs='?',
                            choices=['yes', 'y', 'no', 'n', 'toggle', 't'],
                            default='toggle',
                            help='the mute state. \
                                  Either \'yes\', \'no\' or \'toggle\', \
                                  default toggle')

    @property
    def short_description(self):
        return 'Set the mute state'

# vim: ft=python ts=8 sts=4 sw=4 et:
