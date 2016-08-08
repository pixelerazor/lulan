#!/usr/bin/python3

import http.server

PORT = 8000

handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ['/cgi-bin']
httpd = http.server.HTTPServer( ("", PORT), handler)
try:
    print ("Server Started at port:", PORT)
    httpd.serve_forever()
except KeyboardInterrupt:
    print('\nShutting down server')
    httpd.socket.close()
