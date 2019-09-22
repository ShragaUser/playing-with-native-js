import http.server
import socketserver
import os
import signal
from subprocess import Popen, PIPE

def main():
    PORT = 3000
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("starting development server at port", PORT)
        httpd.serve_forever()

if __name__ == "__main__":
    main()
