from app import app
from flask import render_template


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/faves')
def test():
    fav_ghibli = {'Princess Mononoke': 'https://www.ghibli.jp/gallery/mononoke015.jpg',
    'Nausicaa of the Valley of the Wind': 'https://www.ghibli.jp/gallery/nausicaa044.jpg',
    'Kiki\'s Delivery Service': 'https://www.ghibli.jp/gallery/majo024.jpg',
    'Spirited Away': 'https://www.ghibli.jp/gallery/chihiro045.jpg',
    'Ponyo': 'https://www.ghibli.jp/gallery/ponyo028.jpg'}
    return render_template('faves.html', fav_ghibli = fav_ghibli)