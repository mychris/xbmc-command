# -*- coding: utf-8 -*-

from . import core

class Command(core.Command):

    def call(self, args):
        if args.displaytime < 1500:
            args.displaytime = 1500
        self.xbmc.GUI.ShowNotification({'title':args.title,
                                        'message':args.message,
                                        'displaytime':args.displaytime})

    def create_parser(self, parser):
        parser.prog = '%s notification' % core.PROG
        parser.description = 'Shows a GUI notification.'

        parser.add_argument('--title', dest='title', metavar='<title>',
                            default='xbmc-command',
                            help='the title of the notification, \
                                  default \'xbmc-command\'')

        parser.add_argument('--message', dest='message', required=True,
                            metavar='<message>',
                            help='the message of the notification')

        parser.add_argument('--time', dest='displaytime', default=5000,
                            type=int, metavar='<millis>',
                            help='the time in milliseconds the notification \
                                  will be visible')

    @property
    def short_description(self):
        return 'Shows a GUI notification'

# vim: ft=python ts=8 sts=4 sw=4 et:
