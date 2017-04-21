# -*- coding: utf-8 -*-

import argparse
import re

from . import core

class Command(core.Command):

    def call(self, args):
        if args.artist:
            self.__call_artist(args.artist, args.dry)
        elif args.album:
            self.__call_album(args.album, args.dry)
        elif args.genre:
            self.__call_genre(args.genre, args.dry)

    def __call_artist(self, artist_regex, dry):
        regex = self.__try_regex(artist_regex)

        sort = {
            'order': 'ascending',
            'ignorearticle': True,
            'method': 'artist'
        }
        self.xbmc.AudioLibrary.GetArtists(params={'sort': sort})
        artists = self.xbmc.recv('AudioLibrary.GetArtists')['result']['artists']
        artists = filter(lambda a: regex.search(a['artist']) != None, artists)

        if not artists:
            raise core.CommandException("No artists found for regex '%s'" %
                                        artist_regex)

        if dry:
            for artist in artists:
                print(artist['artist'].encode('utf-8'))
            return
        self.__play({'artist': map(lambda a: a['artistid'], artists)})

    def __call_album(self, album_regex, dry):
        regex = self.__try_regex(album_regex)
        sort = {
            'order': 'ascending',
            'ignorearticle': True,
            'method': 'album'
        }
        self.xbmc.AudioLibrary.GetAlbums(params={'sort': sort})
        albums = self.xbmc.recv('AudioLibrary.GetAlbums')
        albums = albums['result']['albums']
        albums = filter(lambda a: regex.search(a['label']) != None, albums)
        if not albums:
            raise core.CommandException("No albums found for regex '%s'" %
                                        album_regex)

        if dry:
            for album in albums:
                print(album['label'].encode('utf-8'))
            return
        self.__play({'album': map(lambda a: a['albumid'], albums)})

    def __call_genre(self, genre_regex, dry):
        regex = self.__try_regex(genre_regex)
        sort = {
            'order': 'ascending',
            'ignorearticle': False,
            'method': 'genre'
        }
        self.xbmc.AudioLibrary.GetGenres(params={'sort': sort})
        genres = self.xbmc.recv('AudioLibrary.GetGenres')['result']['genres']
        genres = filter(lambda g: regex.search(g['label']) != None, genres)
        if not genres:
            raise core.CommandException("No genres found for regex '%s'" %
                                        genre_regex)

        if dry:
            for genre in genres:
                print(genre['label'].encode('utf-8'))
            return
        self.__play({'genre': map(lambda g: g['genreid'], genres)})

    def __play(self, play_dict):
        audio_pl = self.__get_playlist()
        self.xbmc.Playlist.Clear(params={'playlistid': audio_pl})

        for item_type, item_ids in play_dict.items():
            if item_type == 'album':
                item_type = 'albumid'
            elif item_type == 'artist':
                item_type = 'artistid'
            elif item_type == 'genre':
                item_type = 'genreid'

            for item_id in item_ids[::-1]:
                self.xbmc.Playlist.Insert(params={
                    'playlistid': audio_pl,
                    'item': {item_type: item_id},
                    'position': 0
                })
        self.xbmc.Player.Open(params={'item': {'playlistid': audio_pl}})

    def __try_regex(self, reg):
        regex_flags = re.IGNORECASE | re.UNICODE
        try:
            return re.compile(reg, regex_flags)
        except:
            raise core.CommandException("Invalid regex '%s'" % reg)

    def __get_playlist(self):
        self.xbmc.Playlist.GetPlaylists()
        playlists = self.xbmc.recv("Playlist.GetPlaylists")
        filtered = list(filter(lambda pl: pl['type'] == 'audio',
                               playlists['result']))
        return filtered[0]['playlistid']

    def create_parser(self, parser):
        parser.prog = '%s play-music' % core.PROG
        parser.formatter_class = argparse.RawTextHelpFormatter
        parser.description = '''Start playing music.

You can either specifiy an artist, album or genre regex.
The MusicLibrary will be scanned and filtered with the specified regex.
The remaining items will be played by the AudioPlayer.  If the regex matches too many items, the process may tak a while, depending
on the size of your MusicLibrary.'''

        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('--artist', metavar='<regex>',
                           help='regex for artist filtering')
        group.add_argument('--album', metavar='<regex>',
                           help='regex for album filtering')
        group.add_argument('--genre', metavar='<regex>',
                           help='regex for genre filtering')

        parser.add_argument('--dry', action='store_true', default=False,
                            help='prints the filtered items, but does not start playing them')

    @property
    def short_description(self):
        return 'Start playing music'

# vim: ft=python ts=8 sts=4 sw=4 et:
