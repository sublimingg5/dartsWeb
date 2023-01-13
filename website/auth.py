from flask import Blueprint, render_template, request, flash, redirect, url_for
import re
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Player
from . import db


def only_letters_and_spaces(string):
    return bool(re.match(r'^[a-zA-Z _-]+$', string))

def onlyNumbers(string):
    return bool(re.match(r'^([\s\d]+)$', string))

auth = Blueprint('auth', __name__)

@auth.route('/create-player', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        name = request.form.get('name')
        lastname = request.form.get('lastname')
        pin = request.form.get('pin')

        if not len(username) > 2 or not len(username) < 20 or not only_letters_and_spaces(username):
            flash('The username must be between 2 and 20 characters. Only letters and spaces are allowed', category='error')
        elif not len(name) > 2 or not len(name) < 20 or not only_letters_and_spaces(name):
            flash('The name must be between 2 and 20 characters. Only letters and spaces are allowed', category='error')
        elif not len(lastname) > 2 or not len(lastname) < 20 or not only_letters_and_spaces(lastname):
            flash('The last name must be between 2 and 20 characters. Only letters and spaces are allowed', category='error')
        else:
            newPlayer = Player(username=username, name=name, lastname=lastname, pin=generate_password_hash(pin, method='sha256'))
            db.session.add(newPlayer)
            db.session.commit()
            flash('Player created!', category="success")
            return redirect(url_for('views.home'))
    
    return render_template("create-player.html")

