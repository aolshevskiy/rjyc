package com.epam.rjyc;

import org.python.util.PythonInterpreter;

public class Server {
  private int port;
  private Object context;
  public Server(int port, Object context) {
    this.port = port;
    this.context = context;
  }
  public void start() {
    PythonInterpreter i = new PythonInterpreter();
    i.set("port", port);
    i.set("context", context);
    i.exec("from com.epam.rjyc import Server; Server(port, context).start()");
  }
}