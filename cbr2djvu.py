#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil
import sys
from subprocess import call
import tempfile
import magic

env = os.environ.copy()
env['MAGICK_TMPDIR'] = tempfile.mkdtemp(dir=os.getcwd())


def convert(filename):
    directory = tempfile.mkdtemp()
    os.chdir(directory)
    filename = os.path.join(old_directory, filename)
    m = mime.from_file(filename)
    if m == 'application/x-rar':
        call(['rar', 'e', filename])
    else:

        call(['unzip', '-j', filename])
    ll = os.listdir(directory)
    inner_path = os.path.join(directory, ll[0])

    name = os.path.splitext(filename)[0] + '.djvu'

    call([
        'convert',
        '-limit',
        'memory',
        '1',
        '-limit',
        'map',
        '1',
        '*',
        'foo.pdf',
    ], env=env)
    call(['pdf2djvu', 'foo.pdf', '-o', name])
    call(['mv', os.path.join(inner_path, name), old_directory])

    shutil.rmtree(directory)


if __name__ == '__main__':
    mime = magic.Magic(mime=True)
    old_directory = os.getcwd()
    for fn in sys.argv[1:]:
        convert(fn)
    shutil.rmtree(env['MAGICK_TMPDIR'])
