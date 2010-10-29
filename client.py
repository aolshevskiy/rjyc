from cmd import Cmd as BaseCmd
from code import InteractiveConsole as BaseInteractiveConsole
import re, sys
from xmlrpclib import ServerProxy

class Cmd(BaseCmd):
    reg = re.compile('^\s*')
    def __init__(self, host, port):
        BaseCmd.__init__(self)
        self.s = ServerProxy('http://%s:%d' % (host, int(port)))
        self.prompt = '>>> '
        self.leading_ws = ''
        self.is_empty = False

    def precmd(self, line):
        self.leading_ws = self.reg.match(line).group(0)
        self.is_empty = (line == '')
        return line
        
    def default(self, line):
        if(self.is_empty):
            line = ''        
        line = self.leading_ws + line
        (result, output) = self.s.push(line)
        self.prompt = ('... ' if result else '>>> ')
        sys.stdout.write(output)

if __name__ == '__main__':
    HOST, PORT = sys.argv[1:]
    Cmd(HOST, PORT).cmdloop()
