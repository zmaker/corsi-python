from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib

class myRequestHandler (BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
                
        self.wfile.write(b"<html>")
        self.wfile.write(b"<head>")    
        self.wfile.write(b"<title>POST data</title>")
        self.wfile.write(b"</head>")
        self.wfile.write(b"<body>")
        self.wfile.write(b"<form method='POST'>")
        self.wfile.write(b"<span>Nome: </span><input name='nome'>")
        self.wfile.write(b"<button>Invia</button>")
        self.wfile.write(b"</form>")
        self.wfile.write(b"</body>")
        self.wfile.write(b"</html>")
        return
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        (input, value) = self.rfile.read(content_length).decode('utf-8').split('=')
        value = urllib.parse.unquote_plus(value)
        
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
        
        self.wfile.write(b"<html>")
        self.wfile.write(b"<head>")    
        self.wfile.write(b"<title>Hello</title>")
        self.wfile.write(b"</head>")
        self.wfile.write(b"<body>")
        self.wfile.write(b"<H1>Ciao, "+bytes(value, 'utf-8'))
        self.wfile.write(b"</H1>")
        self.wfile.write(b"<a href='/'>back</a>")
        self.wfile.write(b"</body>")
        self.wfile.write(b"</html>")
        

def run():
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, myRequestHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    print("http://127.0.0.1:8081/")
    run()

