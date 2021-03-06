#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-築城院 真鍳'

import sys #---------------------#
from time import sleep #---------#
from wget import download #------#
from subprocess import Popen #---#
from multiprocessing import Pool #


def fastprint(string):
    """Print chars
    """
    for char in string + '\n':
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(1./30)


def multi(photo):
    """multiprocessing
    """
    pool = Pool()
    pool.map(download, photo)
    pool.close()
    pool.join()


def termin(sec, photo):
    """Open and Close pictures
    """
    viewer = Popen(['feh', photo])
    sleep(sec)
    viewer.terminate()
    viewer.kill()
