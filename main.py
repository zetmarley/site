from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8080
with open('index.html', 'r') as file:
    html_as_string = file.read()
class MyServer(BaseHTTPRequestHandler):

    def __get_html_content(self):
        return
    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        page_content = html_as_string
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print('Server started http://%s:%s' % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print('Server stopped')
site.close()