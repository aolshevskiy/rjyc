import javax.servlet.http.*;
import java.util.*;
import java.io.*;
import net.rjyc.Server;

public class Hello extends HttpServlet {
  public final Map<String, String> links = new HashMap<String, String>();
  {
    links.put("Python", "http://python.org");    
    links.put("Java", "http://java.net");
    Thread t = new Thread() {
      @Override public void run() {
        Map<String, Object> locals = new HashMap<String, Object>();
        locals.put("this", Hello.this);
        new Server("localhost", 8081, locals).start();
      }
    };
    t.start();
  }
  @Override protected void doGet(HttpServletRequest request, HttpServletResponse response)
    throws IOException {
    PrintWriter writer = response.getWriter();
    for(Map.Entry<String, String> e: links.entrySet())
      writer.println("<a href=\""+e.getValue()+"\">"+e.getKey()+"</a>");
    writer.close();
  }
}