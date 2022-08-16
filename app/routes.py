from app import app
from flask import render_template


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/faves')
def test():
    fav_ghibli = ['Princess Mononoke', 
    'Nausicaa of the Valley of the Wind',
    'Kiki\'s Delivery Service',
    'Spirited Away',
    'Ponyo']
    return render_template('faves.html', fav_ghibli = fav_ghibli)