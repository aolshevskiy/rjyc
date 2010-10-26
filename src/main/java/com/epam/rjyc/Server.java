package com.epam.rjyc;

import org.python.util.PythonInterpreter;

public class Server {
  private int port;
  private Object context;
  private PythonInterpreter i;
  public PythonInterpreter getInterpreter() {
    return i;
  }
  public Server(int port, Object context) {
    this.port = port;
    this.context = context;
    i = new PythonInterpreter();
    i.set("port", port);
    i.set("context", context);
  }
  public void start() {    
    i.exec("from com.epam.rjyc import Server; Server(port, context).start()");
  }
}