#http://127.0.0.1:8081/index.html
#http://127.0.0.1:8081/led?stato=acceso&colore=rosso&

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        
        data = urlparse(self.path)
        print(data.query)
        parametri = parse_qs(data.query)
        print(parametri)
        
        message = "<html>"\
                  "<body>"\
                  "<h1>Parametri</h1>"
        
        if '/led' in self.path:
            msg = "Stato del LED: "
            state = 'off'
            color = 'white'
            
            if 'stato' in parametri:
                state = parametri['stato'][0]
            if 'colore' in parametri:
                color = parametri['colore'][0]
            
            if (state == 'on'):
                msg += "ON"
            else:
                msg += "OFF"
                
            message += "<p>"+msg+"</p>"
            message += f"<div style='width:50; height:50; background:{color};'></div>"
            message += "</body></html>"
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
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
