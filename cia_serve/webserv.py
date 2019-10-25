import argparse
import glob
import os

from flask import Flask

app = Flask(__name__)

SCAN_DIRECTORY = '.'

@app.route('/')
def homepage():
    romdir = '**/*.cia'
    roms = glob.glob(romdir, recursive=True)
    roms = list([path.split(os.path.sep) for path in roms])

    return '<br/>'.join([' | '.join(path) for path in roms])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A small HTTP Server to host '+
                                     'CIA files for install with FBI')
    parser.add_argument('--port', '-p', help='Port to run the webserver on. '+
                        'Defaults to 5000', dest='port', action='store',
                        type=int, default=5000)
    parser.add_argument('--dir', '-d', help='Directory to scan for CIA files. '+
                        'Defaults to current directory', dest='directory',
                        action='store', type=str, default='.')
    args = parser.parse_args()
    port = args.port
    SCAN_DIRECTORY = args.directory
    os.chdir(SCAN_DIRECTORY)
    app.run('0.0.0.0', port=port)
