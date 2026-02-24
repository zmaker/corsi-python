from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime

class myRequestHandler (BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
        
        dt = datetime.now()
        dstr = dt.strftime("%d/%m/%Y %H:%M:%S")
        
        msg = "<html>"
        msg += "<head>"    
        msg += "<title>Ora esatta</title>"
        msg += "<meta http-equiv='refresh' content='1'>"
        msg += "</head>"
        msg += "<body>"
        msg += "<h1>" + dstr + "</h1>"
        msg += "</body>"
        msg += "</html>"
        self.wfile.write(bytes(msg, "utf8"))
        return

def run():
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, myRequestHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    print("http://127.0.0.1:8081/")
    run()
