#!python2.7

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import urlparse, parse_qs
import json

class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # パスとクエリパラメータを取得
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)

        # 引数を取得
        argument_value = query_params.get('argument_name', ['default_value'])[0]

        # レスポンスを構築
        response_data = {'message': 'Hello from the API with argument: {}'.format(argument_value)}
        response_body = json.dumps(response_data)

        # CORSヘッダを設定
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # すべてのオリジンからのアクセスを許可
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')  # 許可するHTTPメソッド
        self.send_header('Access-Control-Allow-Headers', 'Content-type')  # 許可するヘッダー
        self.end_headers()

        # レスポンスボディを送信
        self.wfile.write(response_body)

def run_server():
    port = 5000
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleRequestHandler)
    print('Starting server on port {}...'.format(port))
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()

