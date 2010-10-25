import code, socket, sys

class Stdout(object):
    def __init__(self, sock):
        self.sock = sock
    def write(self, bs):
        result = self.sock.write(bs)
        self.sock.flush()
        return result
class Server(object):
    def __init__(self, port, context):
        self.port = port
        self.context = context
    def start(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            s.bind(("0.0.0.0", self.port))
            s.listen(1)
            while(True):
                (cs, addr) = s.accept()
                try:
                    self.handle_conn(cs)
                finally:
                    cs.close()
        finally:
            s.close()
    def handle_conn(self, s):
        f = s.makefile('rw')
        try:
            sys.stdin = f
            sys.stdout = Stdout(f)
            sys.stderr = f
            code.interact(local = {"context": self.context})
        finally:
            f.close()
        
            
