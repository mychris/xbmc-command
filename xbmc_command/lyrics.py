# -*- coding: utf-8 -*-

import argparse
import sys
from . import core

class Command(core.Command):

  def call(self, args):
    player = self.get_active_player_id()
    if player < 0:
      raise core.CommandException("No active player found.")

    player = self.__get_player_props(player)
    playlist = self.__get_playlist(player)

    if playlist['lyrics']:
      self.__print(playlist['artist'][0], playlist['album'], playlist['title'],
          playlist['lyrics'])
      return

    if args.plyr:
      res = self.__try_plyr(playlist['artist'][0], playlist['album'], playlist['title'])
      if res:
        self.__print(playlist['artist'][0], playlist['album'], playlist['title'],
          res)
        return

    raise core.CommandException("No lyrics found.")

  def __get_player_props(self, playerid):
    self.xbmc.Player.GetProperties({'playerid': playerid, 'properties':
      ['type', 'playlistid', 'position']})

    player_props = self.xbmc.recv('Player.GetProperties')
    if not 'result' in player_props:
      raise core.CommandException("Error receiving player properties.")

    player_props = player_props['result']

    if player_props['type'] != 'audio':
      raise core.CommandException("Active player is not an audio player.")

    if player_props['playlistid'] < 0 or player_props['position'] < 0:
      raise core.CommandException("No song found")

    player_props['playerid'] = playerid
    return player_props

  def __get_playlist(self, player_props):
    self.xbmc.Playlist.GetItems({'playlistid':player_props['playlistid'],
      'limits': {'start': player_props['position'],
        'end': player_props['position'] + 1},
      'properties': ['title', 'artist', 'album', 'lyrics']})

    playlist = self.xbmc.recv('Playlist.GetItems')

    if not 'result' in playlist:
      raise core.CommandException("Error receiving playlist properties.")

    if not 'items' in playlist['result'] or not playlist['result']['items']:
      raise core.CommandException("Error receiving current song from playlist.")

    return playlist['result']['items'][0]

  def __try_plyr(self, artist, album, title):
    try:
      import plyr
    except ImportError as e:
      return

    qry = plyr.Query(artist=artist, album=album, title=title,
        timeout=1, get_type='lyrics')
    items = qry.commit()

    if not items:
      raise core.CommandException("No lyrics found with plyr.")

    return items[0].data

  def __print(self, artist, album, title, lyrics):
    if not lyrics:
      return False

    sys.stdout.write('Artist: %s\nAlbum: %s\nTitle: %s\n\n%s\n' % \
        (artist, album, title, lyrics))
    return True

  def create_parser(self, parser):
    parser.prog = '%s lyrics' % core.prog
    parser.description = 'Requests and prints the lyrics of the current song.'

    parser.add_argument('--no-plyr', dest='plyr', action='store_false',
        default=True, help='do not use plyr')

    return parser

  @property
  def short_description(self):
    return 'Get the lyrics of the current song.'

# vim: ft=python ts=2 sts=2 sw=2 et:
