# -*- coding: utf-8 -*-

import json
import sys

from . import core

class Command(core.Command):

    def call(self, args):
        ident = args.id if args.id else args.method
        method = args.method.split('.')
        if len(method) != 2:
            raise core.CommandException("Invalid method name '%s'" % args.method)

        req = self.xbmc.__getattr__(method[0]).__getattr__(method[1])

        try:
            params = json.loads(args.params)
        except ValueError:
            raise core.CommandException("Given parameters are not a valid json object")

        params = {"params": params, "id": ident}

        req(**params)
        answer = self.xbmc.recv(ident)

        sys.stdout.write(json.dumps(answer))
        sys.stdout.write('\n')

    def create_parser(self, parser):
        parser.prog = '%s rpc' % core.PROG
        parser.description = '''Sends an arbitrary JSON RPC to the XBMC and prints
        the answer to the stdout. An exit code of 0 does not indicate that the
        method has been executet correctly. It just indicates, the the format of the
        method name and the parameters are correct.
        '''

        parser.add_argument('method', metavar='<method>',
                            help='the RPC method name. \
                                  Namespace and Method name seperated with a \
                                  "dot" (.).')

        parser.add_argument('params', metavar='<params>',
                            nargs='?', default='{}',
                            help='the parameters. Encoded as JSON object. \
                                  Defaults to {} if omitted')

        parser.add_argument('--id', dest='id', metavar='<request id>',
                            help='the id of the request. \
                                  Defaults to the given method name')


        return parser

    @property
    def short_description(self):
        return 'Send an arbitrary JSON RPC'

# vim: ft=python ts=8 sts=4 sw=4 et:
