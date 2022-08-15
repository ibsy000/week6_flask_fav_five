from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World</h1>'


@app.route('/test')
def test():
    return '<h1>This is a test</h1>'