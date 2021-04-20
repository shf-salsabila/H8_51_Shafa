from flask import Flask
app = Flask(__name__)


@app.route('/') #root
def hello_world():
    return 'Hello, World!!!!!'

@app.route('/hello')
def hello():
    return 'Hello, user!'