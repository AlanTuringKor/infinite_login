from flask import Blueprint, render_template, request, jsonify
from .models import Level
from . import db
import random

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('login.html')

@main.route('/login', methods=['POST'])
def login():
    data = request.json
    level = data['level']
    
    # In a real app, you'd validate the credentials here
    success = random.random() < 0.8  # 80% chance of success

    if success:
        next_level = Level.query.get(level + 1)
        if next_level:
            return jsonify({
                'success': True,
                'nextLevel': {
                    'id': next_level.id,
                    'memeEra': next_level.meme_era,
                    'persona': next_level.persona,
                    'captcha': next_level.captcha,
                    'year': next_level.year,
                    'language': next_level.language,
                    'task': next_level.task
                }
            })
        else:
            return jsonify({'success': True, 'completed': True})
    else:
        return jsonify({'success': False})

def create_levels():
    if Level.query.count() == 0:
        levels = [
            Level(meme_era="GeoCities", persona="Yourself", captcha="Toaster", year=2024, language="English", task="Solve: 2 + 2 = ?"),
            Level(meme_era="MySpace", persona="Pirate", captcha="Quantum Computer", year=1985, language="L33tspeak", task="Write a haiku"),
            Level(meme_era="Doge", persona="Alien", captcha="Sentient Cloud", year=2077, language="Emoji", task="Describe your spirit animal"),
            Level(meme_era="Distracted Boyfriend", persona="Talking Dog", captcha="Time Traveler", year=1692, language="Klingon", task="Invent a new color"),
            Level(meme_era="Modern Minimalist", persona="Superhero", captcha="Meme Lord", year=3030, language="Elvish", task="Explain why pizza is round"),
            # New layers
            Level(meme_era="Retro Gaming", persona="8-bit Hero", captcha="Sentient Pixel", year=1985, language="Binary", task="Defeat the final boss using only emojis"),
            Level(meme_era="Social Media", persona="Influencer", captcha="Viral Meme", year=2023, language="Hashtags", task="Create a 15-second dance challenge"),
            Level(meme_era="Time Paradox", persona="Future You", captcha="Temporal Anomaly", year=2525, language="Reverse English", task="Send a message to past you without creating a paradox"),
            Level(meme_era="Culinary Web", persona="Master Chef", captcha="Sentient Soufflé", year=2099, language="Food Puns", task="Invent a dish that represents your personality"),
            Level(meme_era="Mythical Internet", persona="Legendary Creature", captcha="Cryptid Coder", year=1313, language="Runic", task="Craft a magical spell using only programming languages")
        ]
        db.session.bulk_save_objects(levels)
        db.session.commit()