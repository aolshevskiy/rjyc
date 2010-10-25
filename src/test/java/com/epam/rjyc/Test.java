package com.epam.rjyc;

public class Test {
  public static void main(String [] args) {
    Test test = new Test();
    new Server(8080, test).start();
  }
}