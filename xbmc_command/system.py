# -*- coding: utf-8 -*-

import argparse
import sys
from . import core

class Command(core.Command):

  def call(self, args):
    if args.command == 'quit':
      self.xbmc.Application.Quit()
    elif args.command == 'shutdown':
      self.xbmc.System.Shutdown()
    elif args.command == 'reboot':
      self.xbmc.System.Reboot()
    elif args.command == 'suspend':
      self.xbmc.System.Suspend()
    elif args.command == 'hibernate':
      self.xbmc.System.Hibernate()
    elif args.command == 'infos':
      labels = self.__get_infos()

      sys.stdout.write('XBMC version: %s\n' % labels['System.BuildVersion'])

      sys.stdout.write('XBMC build date: %s\n' % labels['System.BuildDate'])

      sys.stdout.write('System kernel: %s\n' % labels['System.KernelVersion'])

      sys.stdout.write('Uptime: %s\n' % labels['System.Uptime'])

      sys.stdout.write('Total uptime: %s\n' % labels['System.TotalUptime'])

      cpu = labels['System.CPUTemperature']
      gpu = labels['System.GPUTemperature']
      symbol = labels['System.TemperatureUnits']
      sys.stdout.write('CPU temperature: %s%s\n' % (cpu, symbol))
      sys.stdout.write('GPU temperature: %s%s\n' % (gpu, symbol))

      sys.stdout.write('Fan speed: %s\n' % labels['System.FanSpeed'])
      sys.stdout.write('IP address: %s\n' % labels['Network.IPAddress'])
      sys.stdout.write('MAC address: %s\n' % labels['Network.MacAddress'])
    else:
      raise core.CommandException('Invalid command \'%s\'' % args.command)

  def __get_infos(self):
    self.xbmc.XBMC.GetInfoLabels({'labels': ['System.BuildVersion',
      'System.BuildDate', 'System.KernelVersion', 'System.Uptime',
      'System.TotalUptime', 'System.CPUTemperature', 'System.GPUTemperature',
      'System.TemperatureUnits', 'System.FanSpeed',
      'Network.IPAddress', 'Network.MacAddress']})
    ret = self.xbmc.recv('XBMC.GetInfoLabels')

    if not ret['result']['System.KernelVersion'] == 'Busy':
      return ret['result']
    return self.__get_infos()

  def create_parser(self, parser):
    parser.prog = '%s system' % core.prog
    parser.description = 'Handle the XBMC system.'
    parser.formatter_class = argparse.RawTextHelpFormatter
    parser.epilog = """Avaiable commands are:
  quit       Quit the XBMC Mediacenter application
  shutdown   Shutdown the system
  reboot     Reboot the system
  suspend    Suspend the system
  hibernate  Hibernate the system
  infos      Print XBMC system info labels
"""

    parser.add_argument('command', metavar='<command>',
        choices=['quit', 'shutdown', 'reboot', 'suspend', 'hibernate', 'infos'],
        help='the action to perform.')

  @property
  def short_description(self):
    return 'Call system procedure'

# vim: ft=python ts=2 sts=2 sw=2 et:
