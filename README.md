xbmc-command
============

A simple terminal XBMC command client. Connects to the XBMC Mediacenter via
TCP and sends JSON-RPC requests. The client is not interactive and can only
run one command per execution.

It can handle tasks like 'volume up' or 'play youtube video'.
See the help for all available commands.

Installation
------------

run `# python setup.py install` in the root directory of this repository.

Arch Linux users can use the PKGBUILD-git file to create a package.

    $ wget https://raw.github.com/mychris/xbmc-command/master/PKGBUILD-git
    $ makepkg -p PKGBUILD-git

If you want to use plyr, the lib must be installed (no runtime error if the
module is not found). See Optional Dependencies.

A configuration file can be used to specify the host, port and timeout.
It should be installed in ROOT/usr/share/doc/xbmc-command/xbmc-command.cfg.
Just copy it to ~/.config/xbmc-command.cfg and set the preferences.

Usage
-----

    $ xbmc-command --help
    usage: xbmc-command [--host <host>] [--port <port>] [--timeout <sec>]
                        [--help] [--version] <command> [args]

    Connects to the XBMC Mediacenter at <host>:<port> via TCP
    and executes the specified command.

    If --host, --port or --timeout is not present and a config file
    is present in ~/.config/xbmc-command.cfg, the values specified
    in this file will be used.

    Optional arguments:
      --host <host>     connect to server at host <host>
      --port <port>     connect to server at port <port>
      --timeout <sec>   wait <sec> till timeout, default 5
      --help            show this help message and exit
      --version         output version information and exit

    Available commands are:
      mute              Toggle mute
      volume            Set or increment/decrement the volume
      play-pause        Toggle play/pause
      next              Go to the next item in the playlist
      prev              Go to the previous item in the playlist
      system            Call system procedure
      youtube           Play a youtube video
      slideshow         Starts a Picture slideshow
      lyrics            Get the lyrics of the current song.
      notification      Shows a GUI notification
      scan              Scans the XBMC library

    See 'xbmc-command <command> --help' for more information
    on a specific command.

Dependencies
------------

* Python2.7
* XBMC 12.1 "Frodo" (might work with older versions too) <http://xbmc.org/>

Optional Dependencies
---------------------

* plyr: Retrieve lyrics with plyr (<https://github.com/sahib/python-glyr>)

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

