from SimpleXMLRPCServer import *
from os import path
from code import InteractiveConsole as BaseInteractiveConsole

class Stdout(object):
    """Замена stdout для буферизации вывода в строку"""
    def __init__(self):
        self.buffer = ''
    
    def get_buffer(self):
        """Получаем накопленный буфер и сбрасываем его"""
        bc = self.buffer
        self.buffer = ''
        return bc
    
    def write(self, bs):
        """Пишем в буфер вместо стандартного вывода"""
        self.buffer += bs
        return len(bs)

class InteractiveConsole(BaseInteractiveConsole):
    """Интерактивная консоль, возращает вывод выполнения команды"""
    
    def __init__(self, locals):
        """Принимаем контекст выполнения консоли"""
        BaseInteractiveConsole.__init__(self, locals)
        self.stdout = sys.stdout = sys.stderr = Stdout() #Заменяем стандартные потоки собственной реализацией
        
    def push(self, line):
        result = BaseInteractiveConsole.push(self, line)
        return (result, self.stdout.get_buffer()) #Возвращаем вывод вместе с результатом



class Server(SimpleXMLRPCServer):
    """XMLRPC-сервер, поставляющий в сеть методы интерактивной консоли"""
    
    def __init__(self, ls, *args, **kwargs):
        SimpleXMLRPCServer.__init__(self, *args, **kwargs)
        self.register_introspection_functions()
        self.register_instance(InteractiveConsole(ls)) #Регистрируем экземпляр консоли как обработчик с передачей контекста
