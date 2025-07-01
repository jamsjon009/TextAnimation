from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import os
from generator import generate_text_animation

PORT = 8002

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('templates/index.html', 'r') as f:
                self.wfile.write(f.read().encode())
        elif self.path.startswith("/static/"):
            try:
                filepath = self.path.lstrip("/")
                with open(filepath, 'rb') as f:
                    self.send_response(200)
                    if filepath.endswith(".css"):
                        self.send_header('Content-type', 'text/css')
                    self.end_headers()
                    self.wfile.write(f.read())
            except FileNotFoundError:
                self.send_error(404)
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == "/":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            fields = parse_qs(post_data.decode())

            title = fields.get('title', [''])[0]
            content = fields.get('content', [''])[0]
            size = fields.get('size', ['youtube'])[0]  # ✅ Add this line
            lines = content.strip().split('\n')

            # ✅ Pass the selected size
            output_file = generate_text_animation(title, lines, size=size)

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            response = f"""
            <html>
            <body style='font-family:sans-serif; text-align:center;'>
                <h2>Video generated successfully!</h2>
                <p><strong>File saved to:</strong><br>{output_file}</p>
                <a href="/">Back</a>
            </body>
            </html>
            """
            self.wfile.write(response.encode())


if __name__ == "__main__":
    os.makedirs("videos", exist_ok=True)
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"✅ Server running at http://127.0.0.1:{PORT}")
    httpd.serve_forever()
