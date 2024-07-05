from . import db

class Level(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meme_era = db.Column(db.String(100), nullable=False)
    persona = db.Column(db.String(100), nullable=False)
    captcha = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    language = db.Column(db.String(100), nullable=False)
    task = db.Column(db.String(200), nullable=False)