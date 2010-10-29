import sys
import os
from os.path import join, dirname, realpath
SCRIPTDIR = dirname(sys.argv[0])
sys.path[0:0] = [join(SCRIPTDIR, '..', 'src', 'main', 'python')]
from rjyc.server import Server

if __name__ == '__main__':
    SCRIPT, HOST, PORT = sys.argv
    f = file(join(SCRIPTDIR, 'pid'), 'w')
    f.write(str(os.getpid()))
    f.close()
    server = Server((HOST, int(PORT)), logRequests = False)
    server.serve_forever()
