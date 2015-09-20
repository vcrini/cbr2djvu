#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from subprocess import call
import tempfile


def convert(filename):
    directory = tempfile.mkdtemp()
    os.chdir(directory)
    filename = os.path.join(old_directory, filename)
    call(['rar', 'x', filename])
    ll = os.listdir(directory)
    inner_path = os.path.join(directory, ll[0])

    # if there is a directory go inside

    if len(ll) == 1 and os.path.isdir(inner_path):
        os.chdir(inner_path)
    name = os.path.splitext(filename)[0] + '.djvu'
    call(['convert', '*', 'foo.pdf'])
    call(['pdf2djvu', 'foo.pdf', '-o', name])
    call(['mv', os.path.join(inner_path, name), old_directory])


if __name__ == '__main__':
    old_directory = os.getcwd()
    convert(sys.argv[1])
