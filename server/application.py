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


if __name__ == '__main__':
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as server:
        print("serving at port", PORT)
        server.serve_forever()
