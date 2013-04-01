xbmc-command
============

A simple terminal XBMC command client. Connects to the XBMC Mediacenter via
TCP and sends JSON-RPC requests. The client is not interactive and can only
handle one command per execution.

It is designed to handle simple tasks like 'volume up' or 'play next song'.

Installation
------------

Usage
-----

    $ xbmc-command --help
    usage: xbmc-command --host HOST --port PORT [--timeout SEC] [--help]
                        [--version]
                        {mute,next,play-pause,prev,volume} ...

    optional arguments:
        --host HOST           connect to server at host
        --port PORT           connect to server at port
        --timeout SEC         wait SEC till timeout
        --help                show this help message and exit
        --version             show program's version number and exit

    commands:
        valid XBMC commands

        {mute,next,play-pause,prev,volume}
          mute                toggle play/pause
          next                go to next item in playlist
          play-pause          toggle play/pause
          prev                go to previous item in playlist
          volume              set or increment/decrement the volume

Each command has its own --help flag. Use it to show the help of a specific
command.

    $ xbmc-command volume --help

Dependencies
------------

* Python3 (should also run with python 2.7)
* XBMC 12.1 "Frodo" (might work with older versions too)

