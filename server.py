from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/notice.html'
            client_ip = self.client_address[0]
            print(f'Visitor IP: {client_ip}')
        return SimpleHTTPRequestHandler.do_GET(self)

def main():
    PORT = 8081
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, CustomRequestHandler)
    print(f'Serving on port {PORT}')
    httpd.serve_forever()

if __name__ == '__main__':
    main()

