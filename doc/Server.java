package net.rjyc;

import org.python.util.PythonInterpreter;
import java.util.*;

public class Server {
  private PythonInterpreter i;
  public PythonInterpreter getInterpreter() {
    return i;
  }
  public Server(String host, int port) {
    this(host, port, new HashMap<String, Object>());
  }
  public Server(String host, int port, Map<String, Object> locals) {
    i = new PythonInterpreter();
    //устанавливаем аргументы в экземпляр интерпретатора
    i.set("host", host);
    i.set("port", port);
    i.set("ls", locals);
  }
  
  public void start() {
    //запускаем сервер интерактивной консоли
    i.exec("from rjyc import Server; Server(dict(ls), (host, port), logRequests = False).serve_forever()");
  }
}