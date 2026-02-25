from http.server import HTTPServer, BaseHTTPRequestHandler

class myRequestHandler (BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
        
        msg = "Hello Web Python!"
        self.wfile.write(bytes(msg, "utf8"))
        return

def run():
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, myRequestHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    print("http://127.0.0.1:8081/")
    run()