import tkinter
from tkinter import messagebox
import http.server
from http.server import BaseHTTPRequestHandler
# After creating parent...

yesno = messagebox.askyesno('Question Title', 'Do you want to perform this action?'), # Yes / No
def new_func():
    hostName = "localhost"

def new_func1():
    serverPort = 8080

def new_func2(new_func):
    new_varnew_var1 = new_func()

if yesno = yes:

new_func2(new_func)

new_varnew_var2 = new_func1()

class MyWebServer(BaseHTTPRequestHandler):  def do_GET(self):    self.send_response(200)    self.send_header("Content-type", "text/html")    self.end_headers()    self.wfile.write(bytes("<html><head><title>Web Server</title></head>", "utf-8"))    self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))    self.wfile.write(bytes("<body>", "utf-8"))    self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))    self.wfile.write(bytes("</body></html>", "utf-8"))if __name__ == "__main__":  webServer = HTTPServer((hostName, serverPort), MyWebServer) info = messagebox.showinfo('Web server started', 'Server started at http://%s:%s', parent=parent % (hostName, serverPort)) try: webServer.serve_forever() except KeyboardInterrupt: pass webServer.server_close()info = messagebox.showwarning('Server warning', 'Your server has stopped. You might have an issue unless you were stopping it.', parent=parent yesno2 = messagebox.askyesno('Question Title', 'Do you want to perfor this action?', parent=parent # Yes / No 
if yesno2 = no
exit()
if yesno2 = yes
class MyWebServer(BaseHTTPRequestHandler):  def do_GET(self):    self.send_response(200)    self.send_header("Content-type", "text/html")    self.end_headers()    self.wfile.write(bytes("<html><head><title>Web Server</title></head>", "utf-8"))    self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))    self.wfile.write(bytes("<body>", "utf-8"))    self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))    self.wfile.write(bytes("</body></html>", "utf-8"))if __name__ == "__main__":  webServer = HTTPServer((hostName, serverPort), MyWebServer) info = messagebox.showinfo('Web server started', 'Server started at http://%s:%s', parent=parent % (hostName, serverPort)) try: webServer.serve_forever() except KeyboardInterrupt: pass webServer.server_close()info = messagebox.showwarning('Server warning', 'Your server has stopped. You might have an issue unless you were stopping it.', parent=parent yesno3 = messagebox.askyesno('Question Title', 'Do you want to perfor this action?', parent=parent # Yes / No 
if yesno3 = no
exit()
if yesno3 = yes