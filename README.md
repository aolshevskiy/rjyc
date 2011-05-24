# Overview

This is a remote Python console allowing to manipulate your JVM application in runtime. 

See [my article](http://devnest.blogspot.com/2010/10/jython.html) in Russian for more details.

## Maven Artifacts

1. Add following repository definition to `pom.xml`:
    
        <repository>
          <id>Rjyc Repository</id>
          <url>http://siasia.github.com/maven2</url>
        </repository>
				
2. and a dependency itself:

        <dependency>
          <groupId>org.python</groupId>
          <artifactId>rjyc</artifactId>
          <version>1.0-SNAPSHOT</version>
        </dependency>

## Usage

1. Inject the remote console server into the project:

        import net.rjyc.Server;
        import java.util.*;

        public class Test {
          public int test;
          public static void main(String [] args) {
            Map<String, Object> locals = new HashMap<String, Object>() { //create locals for your interpreter
              put("context", new Test());
            };
            /* start the server listening for localhost:8080 
             * with a context variable set to the instance of Test
             */
            new Server("localhost", 8080, locals).start(); 
          }
        }
2. Grab [client.py](https://github.com/siasia/rjyc/raw/master/client.py) and run it like this:

        siasia@siasia ~/projects/rjyc % python2 client.py localhost 8080
        >>> print 1
        1
        >>> for i in range(1, 5):
        ...     print i
        ... 
        1
        2
        3
        4
        >>> context
        Test@7c9586
        >>> context.test
        0
        >>> context.test = 1
        >>> context.test
        1
        >>> context.
        context.__class__         context.__hash__          context.__reduce_ex__     context.equals            context.notifyAll
        context.__delattr__       context.__init__          context.__repr__          context.getClass          context.test
        context.__doc__           context.__ne__            context.__setattr__       context.hashCode          context.toString
        context.__eq__            context.__new__           context.__str__           context.main              context.wait
        context.__getattribute__  context.__reduce__        context.class             context.notify            
        >>> import java
        >>> java.
        java.__name__  java.io        java.lang      java.net       java.nio        java.security  java.util      
        >>> java.io.FileOutputStream('/tmp/test.txt')
        java.io.FileOutputStream@fd5428
