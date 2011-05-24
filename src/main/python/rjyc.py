from SimpleXMLRPCServer import *
from os import path
from code import InteractiveConsole as BaseInteractiveConsole
from rlcompleter import Completer
import __main__

class Stdout(object):
    def __init__(self):
        self.buffer = ''
    def get_buffer(self):
        bc = self.buffer
        self.buffer = ''
        return bc
    def write(self, bs):
        self.buffer += bs
        return len(bs)

class InteractiveConsole(BaseInteractiveConsole):
    def __init__(self, ls):
        BaseInteractiveConsole.__init__(self, ls)
        self.stdout = sys.stdout = sys.stderr = Stdout()
        self.completer = Completer(dict(self.locals))
    def push(self, line):
        result = BaseInteractiveConsole.push(self, line)
        return (result, self.stdout.get_buffer())
    def complete(self, text):
        state = 0
        comps = []
        while True:
            self.completer.namespace = dict(self.locals)
            result = self.completer.complete(text, state)
            if result is None:
                break
            comps.append(result)
            state += 1
        return comps

class Server(SimpleXMLRPCServer):
    def __init__(self, ls, *args, **kwargs):
        SimpleXMLRPCServer.__init__(self, *args, **kwargs)
        self.register_introspection_functions()
        self.register_instance(InteractiveConsole(ls))
