# -*- coding: utf-8 -*-

import sys
from . import core

class Command(core.Command):

  def call(self, args):
    current_song = self.__current_song()

    artist = current_song['MusicPlayer.Artist']
    album = current_song['MusicPlayer.Album']
    title = current_song['MusicPlayer.Title']
    lyrics = current_song['MusicPlayer.Lyrics']

    if not lyrics and not artist and not album and not title:
      raise core.CommandException("No Music playing")

    if not lyrics and artist and album and title:
      lyrics = self.__try_plyr(artist, album, title)

    if lyrics:
      self.__print(artist, album, title, lyrics)
    else:
      raise core.CommandException("No lyrics found.")

  def __current_song(self):
    self.xbmc.XBMC.GetInfoLabels({'labels': ['MusicPlayer.Artist',
      'MusicPlayer.Title', 'MusicPlayer.Album', 'MusicPlayer.Lyrics']})
    result = self.xbmc.recv('XBMC.GetInfoLabels')
    if not 'result' in result:
      raise core.CommandException("Error retrieving info labels")
    return result['result']

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
        (artist, album, title, lyrics.decode('utf-8')))
    return True

  def create_parser(self, parser):
    parser.prog = '%s lyrics' % core.prog
    parser.description = '''Requests and prints the lyrics of the current song.
    If plyr should be used to retrieve the lyrics, it must be properly
    installed.'''

    return parser

  @property
  def short_description(self):
    return 'Get the lyrics of the current song'

# vim: ft=python ts=2 sts=2 sw=2 et:
