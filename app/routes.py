from app import app
from flask import render_template


@app.route('/')
def index():
    return '<h1>Hello World</h1>'


@app.route('/test')
def test():
    return '<h1>This is a test</h1>'