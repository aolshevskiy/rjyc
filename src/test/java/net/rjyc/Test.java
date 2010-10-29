package net.rjyc;

import java.util.*;

public class Test {
  public int test;
  public static void main(String [] args) {
    Map<String, Object> locals = new HashMap<String, Object>();
    locals.put("context", new Test());
    new Server("localhost", 8080, locals).start();
  }
}