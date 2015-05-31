#! /usr/bin/env python3

from os import path

from guafeng.world import World


MAP = path.dirname(__file__) + '/../data/map_01.tmx'

if __name__ == '__main__':
    World(MAP).start()
