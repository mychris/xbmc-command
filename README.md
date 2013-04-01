xbmc-command
============

A simple terminal XBMC command client. Connects to the XBMC Mediacenter via
TCP and sends JSON-RPC requests. The client is not interactive and can only
run one command per execution.

It can handle tasks like 'volume up' or 'play youtube video'.
See the help for all available commands.

Installation
------------

run

    # python setup.py install

in the root directory of this repository.

Arch Linux users can use the PKGBUILD-git file to create a package.

    $ wget https://raw.github.com/mychris/xbmc-command/master/PKGBUILD-git
    $ makepkg -p PKGBUILD-git

Usage
-----

    $ xbmc-command --help
    usage: xbmc-command --host HOST --port PORT [--timeout SEC] [--help]
                        [--version]
                        {mute,next,play-pause,prev,volume,youtube} ...

    optional arguments:
        --host HOST         connect to server at host
        --port PORT         connect to server at port
        --timeout SEC       wait SEC till timeout
        --help              show this help message and exit
        --version           show program's version number and exit

    commands:
      valid XBMC commands

      {mute,next,play-pause,prev,volume,youtube}
        mute                toggle mute
        next                go to the next item in playlist
        play-pause          toggle play/pause
        prev                go to the previous item in playlist
        volume              set or increment/decrement the volume
        youtube             play a youtube video

All commands have their own --help flag. Use it to show the help of a specific
command.

    $ xbmc-command volume --help

Dependencies
------------

* Python3 (should also run with python 2.7)
* XBMC 12.1 "Frodo" (might work with older versions too) <http://xbmc.org/>

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

