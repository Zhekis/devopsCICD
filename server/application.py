"""Module providing a web server with testing capabilities."""

import http.server
import socketserver

PORT = 8000

class TestMe:
    """Simple class for demonstrating unit test functionality."""
    
    def take_five(self):
        """Return the integer 5."""
        return 5
    
    def port(self):
        """Return the server port number."""
        return PORT
    
    def serve_forever(self):
        """Start the web server and serve requests indefinitely."""
        handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("", PORT), handler) as httpd:
            print("serving at port", PORT)
            httpd.serve_forever()

if __name__ == '__main__':
    test_instance = TestMe()
    test_instance.serve_forever()
    # Web server responds to any request with print output, 
    # by default shows client file list in current directory