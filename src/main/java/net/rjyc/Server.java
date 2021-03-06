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
    i.set("host", host);
    i.set("port", port);
    for(Map.Entry<String, Object> entry: locals.entrySet())
      i.set(entry.getKey(), entry.getValue());
  }
  
  public void start() {    
    i.exec("from rjyc import Server; Server(locals(), (host, port), logRequests = False).serve_forever()");
  }
}