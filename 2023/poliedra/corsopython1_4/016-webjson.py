from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        
        data = None
        if '/hello' in self.path:
            data = json.dumps({'hello':'world', 'received':'ok'})
        else:
            data = json.dumps({'error':'not found'})
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(data, "utf8"))
        return

def run():
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print("server attivo")
    httpd.serve_forever()

if __name__ == "__main__":
    print("prova ad aprire: http://127.0.0.1:8081/")
    run()
