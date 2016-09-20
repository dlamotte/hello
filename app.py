from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
<html>
<head>
    <title>hello world!</title>
</head>
<body>
    <h1>hello world!</h1>
</body>
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
