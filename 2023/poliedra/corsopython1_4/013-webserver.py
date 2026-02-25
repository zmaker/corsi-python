from http.server import HTTPServer, BaseHTTPRequestHandler

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = "<html><body><h1>Hello Web!</h1></body></html>"
        self.wfile.write(bytes(message, "utf8"))
        return

def run():
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print("server attivo")
    httpd.serve_forever()

if __name__ == "__main__":
    print("prova ad aprire: http://127.0.0.1:8081/")
    run()