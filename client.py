from cmd import Cmd as BaseCmd
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

    def complete(self, text, state):
        """Return the next possible completion for 'text'.

        If a command has not been entered, then complete against command list.
        Otherwise try to call complete_<command> to get list of completions.
        """
        if state == 0:
            import readline
            origline = readline.get_line_buffer()
            line = origline.lstrip()
            stripped = len(origline) - len(line)
            begidx = readline.get_begidx() - stripped
            endidx = readline.get_endidx() - stripped
            if begidx>=0:
                cmd, args, foo = self.parseline(line)
                if cmd == '':
                    compfunc = self.completedefault
                else:
                    try:
                        compfunc = getattr(self, 'complete_' + cmd)
                    except AttributeError:
                        compfunc = self.completedefault
            else:
                compfunc = self.completenames
            self.completion_matches = compfunc(text, line, begidx, endidx)
        try:
            return self.completion_matches[state]
        except IndexError:
            return None

    def completedefault(self, text, *ignored):
        return self.s.complete(text)

if __name__ == '__main__':
    HOST, PORT = sys.argv[1:]
    Cmd(HOST, PORT).cmdloop()
