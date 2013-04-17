# -*- coding: utf-8 -*-

import argparse
import re
import socket
from . import core

class Command(core.Command):

  def run_command(self, args):
    self.call(args)

  def call(self, args):
    data = 'FFFFFFFFFFFF' + (args.mac.replace(args.mac[2], '') * 16)
    data = bytearray.fromhex(data)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(data, ('<broadcast>', args.port))

  def create_parser(self, parser):
    parser.prog = '%s wake-on-lan' % core.prog
    parser.description = 'turn the XBMC Mediacenter on via Wake-On-Lan.'

    parser.add_argument('mac', metavar='<mac-address>', type=mac_address,
        help='the MAC address of the computer')

    parser.add_argument('--port', dest='port', metavar='<port>', default=7,
        type=port,
        help='Wake-On-Lan port, default 7')

  @property
  def short_description(self):
    return 'Turn the XBMC Mediacenter on via Wake-On-Lan'

def mac_address(val):
  if not re.match('^([0-9A-F]{2}[:-]){5}([0-9A-F]{2})$', val):
    raise argparse.ArgumentTypeError("invalid MAC address value: '%s'" % val)
  return val

def port(val):
  try:
    if int(val) < 0 or int(val) > 65535:
      raise argparse.ArgumentTypeError("invalid port value: '%s'" % val)
    return int(val)
  except ValueError:
    raise argparse.ArgumentTypeError("invalid port value: '%s'" % val)

# vim: ft=python ts=2 sts=2 sw=2 et:
