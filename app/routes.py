from app import app
from flask import render_template


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/faves')
def test():
    fav_ghibli = {'film': [
    {
        'title': 'Princess Mononoke', 
        'image': 'https://www.ghibli.jp/gallery/mononoke015.jpg', 
        'description': 'On a journey to find the cure for a Tatarigami\'s curse, Ashitaka finds himself in the middle of a war between the forest gods and Tatara, a mining colony. In this quest he also meets San, the Mononoke Hime.',
        'link': 'https://play.hbomax.com/page/urn:hbo:page:GXrHUCwY3E6u9KwEAAAAO:type:feature'
    }, 
    {
        'title': 'Nausicaa of the Valley of the Wind',
        'image': 'https://www.ghibli.jp/gallery/nausicaa044.jpg',
        'description': 'After a devastating world war, the Valley of the Wind is one of the last places untouched by the toxic aftermath. Nausicaa fights to restore balance between humans and nature as others seek the destructive power that once ravaged the Earth.',
        'link': 'https://play.hbomax.com/page/urn:hbo:page:GXrHVaQyRPXUYOAEAAABO:type:feature'
    },
    {
        'title': 'Kiki\'s Delivery Service',
        'image': 'https://www.ghibli.jp/gallery/majo024.jpg',
        'description': 'From the legendary Hayao Miyazaki comes the beloved story of a resourceful young witch who uses her broom to create a delivery service, only to lose her gift of flight in a moment of self-doubt.',
        'link': 'https://play.hbomax.com/page/urn:hbo:page:GXrHTGwYHRnUYOAEAAABC:type:feature'
    },
    {
        'title': 'Spirited Away',
        'image': 'https://www.ghibli.jp/gallery/chihiro045.jpg',
        'description': 'When Chihiro is whisked away into a breathtaking world full of spirits and demons, she must use all her wits in order to free herself and her parents from the sorceress Yubaba, in Hayao Miyazaki\'s Academy Award-winning masterpiece.',
        'link': 'https://play.hbomax.com/page/urn:hbo:page:GXrHanAQBunUYOAEAAAB3:type:feature'
    },
    {
        'title': 'Ponyo',
        'image': 'https://www.ghibli.jp/gallery/ponyo028.jpg',
        'description': 'A magical goldfish named Ponyo, the young daughter of a sorcerer father rand a sea-goddess mother, befriends Sosuke. Ponyo yearns to become human to be with Sosuke, but their friendship leads to unintended consequences on both land and sea.',
        'link': 'https://play.hbomax.com/page/urn:hbo:page:GXrWweQmaqDmqwwEAAAAm:type:feature'}
    ]}
    return render_template('faves.html', fav_ghibli = fav_ghibli['film'])