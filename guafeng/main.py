#! /usr/bin/env python3

from os import path

from guafeng.world import create_world


MAP = path.dirname(__file__) + '/../data/map_01.tmx'

if __name__ == '__main__':
    create_world(MAP).start()
