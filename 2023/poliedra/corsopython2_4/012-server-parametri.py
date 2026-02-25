from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class myRequestHandler (BaseHTTPRequestHandler):
    def do_GET(self):
        
        data = urlparse(self.path)
        param = parse_qs(data.query)
        print(param)
        
        msg = "Stato LED:"
        state = "off"
        color = "white"
        
        page = "<html>"
        page += "<head>"    
        page += "<title>Parametri</title>"
        page += "</head>"
        page += "<body>"

        if '/led' in self.path:
            if 'state' in param:
                state = param['state'][0]

            if 'color' in param:
                color = param['color'][0]

            if (state == 'on'):
                msg += "ON"
            else:
                msg += "OFF"
            
            page += "<h1>" + msg + "</h1>"
            page += f"<div style='width:50; height:50; background:{color};'></div>"
            
        
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
                
        
        page += "</body>"
        page += "</html>"
        self.wfile.write(bytes(page, "utf8"))
        return

def run():
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, myRequestHandler)
    httpd.serve_forever()

if __name__ == "__main__":
    print("http://127.0.0.1:8081/")
    run()


#http://127.0.0.1:8081/index.html
#http://127.0.0.1:8081/led?state=on&color=red&
