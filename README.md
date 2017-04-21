xbmc-command
============

A simple terminal Kodi/XBMC command client. Connects to the
Kodi/XBMC Mediacenter via TCP and sends JSON-RPC requests. The client is not
interactive and can only run one command per execution.

It can handle tasks like 'volume up' or 'play youtube video'.
See the help for all available commands.

You can also send arbitrary JSON RPCs and use this program in your own scripts

    xbmc-command rpc XBMC.GetInfoLabels '{"labels": ["MusicPlayer.Artist"]}' --id test

You have to **enable** the JSON-RPC API within Kodi:
http://kodi.wiki/view/JSON-RPC_API#Enabling_JSON-RPC

Installation
------------

run `# python setup.py install` in the root directory of this repository.

Arch Linux users can use the PKGBUILD-git file to create a package.

    $ wget https://raw.github.com/mychris/xbmc-command/master/PKGBUILD-git
    $ makepkg -p PKGBUILD-git

If you want to use plyr, the lib must be installed (no runtime error if the
module is not found). See Optional Dependencies.

A **configuration file** can be used to specify the host, port or timeout.
It should be installed in `ROOT/usr/share/doc/xbmc-command/xbmc-command.cfg`.
Just copy it to `~/.config/xbmc-command.cfg` and set the preferences.

Usage
-----

**help**

    $ xbmc-command --help
    usage: xbmc-command [--host <host>] [--port <port>] [--timeout <sec>] [--help]
                        [--version]
                        <command> ...

    Connects to the XBMC Mediacenter at <host>:<port> via TCP
    and executes the specified command.

    If --host, --port or --timeout is not present and the config
    file ~/.config/xbmc-command.cfg is readable, the values
    specified in this file will be used.

    Optional arguments:
      --host <host>     connect to server at host <host>
      --port <port>     connect to server at port <port>
      --timeout <sec>   wait <sec> till timeout, default 5
      --help            show this help message and exit
      --version         output version information and exit

    Available commands are:
      mute              Set the mute state
      volume            Set or increment/decrement the volume
      play-pause        Toggle play/pause
      play-music        Start playing music
      next              Go to the next item in the playlist
      prev              Go to the previous item in the playlist
      repeat            Set the repeat state
      shuffle           Set the player shuffle mode
      system            Call system procedure
      youtube           Play a youtube video
      twitch            Play a twitch channel
      slideshow         Starts a Picture slideshow
      lyrics            Get the lyrics of the current song
      notification      Shows a GUI notification
      scan              Scans the XBMC library
      wake-on-lan       Turn the XBMC Mediacenter on via Wake-On-Lan
      rpc               Send an arbitrary JSON RPC

    See 'xbmc-command <command> --help' for more information
    on a specific command.

**config**

The config file must be stored in `~/.config/xbmc-command.cfg`.
It consists of the sections *XBMC* and *alias*.

The *XBMC* section may contain the options 'host', 'port' and 'timeout'.
See the help.

The *alias* section contains command aliases. The alias must not be quoted, but
may contain quoted strings as arguments. If a line is indented by one or more
spaces, the line belongs to the previous defined alias.

    y = youtube --quality 1080p

    shutdown = system shutdown

Dependencies
------------

* Python2.7
* Kodi (XBMC) 14.0 "Helix" (might work with older versions too) <http://kodi.tv/>

Optional Dependencies
---------------------

* plyr: Retrieve lyrics with plyr (<https://github.com/sahib/python-glyr>)
  
  if plyr is not properly installed (or not installed at all) xbmc-command will
  not use this library.

Note
----

I use xbmc-command on a daily base. Updates don't come very frequently because
it works for me. If you have any issues or want some feature, create an issue
and let me know (or fork and send a pull request).

License
-------

    Copyright (C) 2013 Christoph Göttschkes <just dot mychris at googlemail dot com>
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

