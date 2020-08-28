# -*- coding: utf-8 -*-

import argparse
import time
import socket
import sys
import json

__prog__ = 'xbmc-command'
PROG = __prog__

__version__ = '0.4.1'
VERSION = __version__

class XBMC(object):

    def __init__(self, host, port):
        self.address = (host, port)
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__buffer = ""
        self.__decode = json.JSONDecoder().raw_decode

        self.settimeout(0)

    def settimeout(self, timeout):
        self.__timeout = timeout
        self.__socket.settimeout(timeout if timeout > 0 else None)

    def connect(self):
        self.__socket.connect(self.address)

    def close(self):
        if self.__socket:
            self.__socket.close()

    def shutdown(self):
        self.__socket.shutdown(socket.SHUT_RDWR)

    def __getattr__(self, key):
        return Rpc(self, key)

    def send(self, req):
        self.__socket.send(bytearray(req, 'utf-8'))

    def recv(self, json_rpc_id):
        start = time.time()

        while True:
            if self.__timeout > 0 and time.time() - start > self.__timeout:
                raise CommandException("read timeout")
            try:
                data = self.__socket.recv(1024)
            except socket.timeout:
                raise CommandException("read timeout")
            if not data:
                return None
            self.__buffer += data.decode('utf-8')

            while True:
                json_result = None
                try:
                    json_result, index = self.__decode(self.__buffer)
                    self.__buffer = self.__buffer[index:]
                except ValueError:
                    break
                if json_result and 'id' in json_result and \
                      json_result['id'] == json_rpc_id:
                    return json_result

        return None

class Rpc(object):

    __REQ__ = '{"jsonrpc":"2.0", "method":"%s", "params":%s, "id":"%s"}'

    def __init__(self, xbmc, method):
        self.__xbmc = xbmc
        self.__method = method

    def __getattr__(self, key):
        return Rpc(self.__xbmc, "%s.%s" % (self.__method, key))

    def __call__(self, *args, **kwargs):
        params = '{}'
        ident = str(kwargs['id']) if 'id' in kwargs else self.__method

        if args:
            params = json.dumps(args[0])
        elif 'params' in kwargs:
            params = json.dumps(kwargs['params'])

        self.__xbmc.send(Rpc.__REQ__ % (self.__method, params, ident))

class CommandException(Exception):

    def __init__(self, msg):
        Exception.__init__(self)
        self.msg = msg

    def __str__(self):
        return self.msg

class Command(object):

    def __init__(self):
        self.xbmc = None

    def call(self, args):
        raise NotImplementedError("Please Implement this method")

    def run_command(self, args):
        try:
            self.xbmc.connect()
        except socket.timeout:
            raise CommandException("Unable to connect to host %s:%s" % \
                (self.xbmc.address[0], self.xbmc.address[1]))
        except socket.error as err:
            self.xbmc.close()
            raise CommandException("Could not open socket: " + err)

        self.call(args)

    def get_active_player_id(self):
        self.xbmc.Player.GetActivePlayers()
        result = self.xbmc.recv('Player.GetActivePlayers')
        if not result:
            raise CommandException('unable to receive active players')
        if len(result['result']) <= 0:
            return -1

        for player in result['result']:
            if player['type'] in ('audio', 'video'):
                return player['playerid']
        return result['result'][0]['playerid']

    @property
    def parser(self):
        parser = argparse.ArgumentParser(add_help=False)
        self.create_parser(parser)
        parser.add_argument('--help', action='help',
                            help='show this help message and exit')
        return parser

    def create_parser(self, parser):
        return parser

    def parse_args(self, args):
        return self.parser.parse_args(args)

    @property
    def short_description(self):
        return ''

# vim: ft=python ts=8 sts=4 sw=4 et:
