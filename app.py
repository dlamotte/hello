from flask import Flask
import socket

app = Flask(__name__)

def get_public_ip():
    sock = socket.socket()
    sock.connect(('google.com', 80))
    return sock.getsockname()[0]

@app.route('/')
def index():
    return '''
<html>
<head>
    <title>hello world!</title>
</head>
<body>
    <h1>hello world! v0.4</h1>
    <p>
        {ip}
    </p>
</body>
</html>
'''.lstrip().format(ip=get_public_ip())

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
