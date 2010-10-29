from cmd import Cmd as BaseCmd
from code import InteractiveConsole as BaseInteractiveConsole
import re, sys
from xmlrpclib import ServerProxy

class Cmd(BaseCmd):
    """Реализация прокси-консоли"""
    reg = re.compile('^\s*')
    def __init__(self, host, port):        
        BaseCmd.__init__(self)
        self.s = ServerProxy('http://%s:%d' % (host, int(port))) #Клиент нашего сервиса
        self.prompt = '>>> ' #Приглашение к вводу
        self.leading_ws = '' #Переменная для ведущих пробелов
        self.is_empty = False #Переменная определяющая пустую команду

    def precmd(self, line):
        """Тестируем различные условия с сырой строкой,
        которая затем фильтруется"""
        self.leading_ws = self.reg.match(line).group(0) #Сохраняем ведущие пробелы, т.к. они фильтруется при передаче в default
        self.is_empty = (line == '') #Пустая ли команда, т.к. пустая команда далее преобразуется в повторение предыдущей
        return line #Выполняем контракт описанный в документации
        
    def default(self, line):        
        if(self.is_empty): #Восстанавливаем пустую строкy
            line = ''
        line = self.leading_ws + line #Восстанавливаем ведущие пробелы
        (result, output) = self.s.push(line) #Выполняем строку в удалённой консоли
        self.prompt = ('... ' if result else '>>> ') #В случае если требуется новый ввод устанавливаем соответствующее приглашение
        sys.stdout.write(output) #Пишем аутпут в аутпут :)

if __name__ == '__main__':
    HOST, PORT = sys.argv[1:]
    Cmd(HOST, PORT).cmdloop()
