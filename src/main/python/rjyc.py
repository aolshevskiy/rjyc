from SimpleXMLRPCServer import *
from os import path
from code import InteractiveConsole as BaseInteractiveConsole

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
    def __init__(self, locals):
        BaseInteractiveConsole.__init__(self, locals)
        self.stdout = sys.stdout = sys.stderr = Stdout()
    def push(self, line):
        result = BaseInteractiveConsole.push(self, line)
        return (result, self.stdout.get_buffer())

class Server(SimpleXMLRPCServer):
    def __init__(self, ls, *args, **kwargs):
        SimpleXMLRPCServer.__init__(self, *args, **kwargs)
        self.register_introspection_functions()
        self.register_instance(InteractiveConsole(ls))
