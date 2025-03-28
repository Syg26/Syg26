import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpExchange;
import java.io.IOException;
import java.io.OutputStream;

public class HelloWorld {
    public static void main(String[] args) throws Exception {
        // Create an HTTP server that listens on port 8001
        HttpServer server = HttpServer.create(new java.net.InetSocketAddress(8001), 0);
        
        // Create a handler for the root context ("/")
        server.createContext("/", new HttpHandler() {
            @Override
            public void handle(HttpExchange exchange) throws IOException {
                String response = "Hello, World!";
                exchange.sendResponseHeaders(200, response.getBytes().length);
                OutputStream os = exchange.getResponseBody();
                os.write(response.getBytes());
                os.close();
            }
        });
        
        // Start the server
        server.start();
        System.out.println("Server started on port 8001");
    }
}
