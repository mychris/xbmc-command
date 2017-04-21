# -*- coding: utf-8 -*-

import argparse

from . import core

class Command(core.Command):

    def call(self, args):
        if args.decrement:
            vol = 'decrement'
        elif args.increment:
            vol = 'increment'
        else:
            vol = args.set

        self.xbmc.Application.SetVolume({'volume':vol})

    def create_parser(self, parser):
        parser.prog = '%s volume' % core.PROG
        parser.description = 'Set or increment/decrement the volume.'

        group = parser.add_mutually_exclusive_group(required=True)

        group.add_argument('--increment', dest='increment',
                           action='store_true', default=False,
                           help='increment the volume')

        group.add_argument('--decrement', dest='decrement',
                           action='store_true', default=False,
                           help='decrement the volume')

        group.add_argument('--set', dest='set',
                           type=parse_range_zero_to_hundred, metavar='<volume>',
                           help='set the volume to <volume> (range 0-100)')

        return parser

    @property
    def short_description(self):
        return 'Set or increment/decrement the volume'

def parse_int(string):
    try:
        return int(string)
    except ValueError:
        raise argparse.ArgumentTypeError("invalid int value: '%s'" % string)

def parse_range_zero_to_hundred(string):
    string = parse_int(string)
    if string < 0 or string > 100:
        raise argparse.ArgumentTypeError(
            "int value %d out of range (0-100)" % string)
    return string

# vim: ft=python ts=8 sts=4 sw=4 et:
