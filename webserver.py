import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

Handler = SimpleHTTPRequestHandler
Server = BaseHTTPServer.HTTPServer
Protocal = "HTTP/1.0"

if sys.argv[1:]:
	port = int(sys.argv[1])
else:
	port = 8080
	
server_address = ('127.0.0.1', port)

Handler.protocal_version = Protocal
httpd = Server(server_address, Handler)
#sa = httpd.socket.getsocketname()
print("Serving HTTP")
httpd.serve_forever()
