from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Flashcard
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        flashcard = request.form.get('flashcard')#Gets the flashcard from the HTML 

        if len(flashcard) < 1:
            flash('flashcard is too short!', category='error') 
        else:
            new_flashcard = Flashcard(data=flashcard, user_id=current_user.id)  #providing the schema for the flashcard 
            db.session.add(new_flashcard) #adding the flashcard to the database 
            db.session.commit()
            flash('flashcard added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-flashcard', methods=['POST'])
def delete_flashcard():  
    flashcard = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    flashcardId = flashcard['flashcardId']
    flashcard = flashcard.query.get(flashcardId)
    if flashcard:
        if flashcard.user_id == current_user.id:
            db.session.delete(flashcard)
            db.session.commit()

    return jsonify({})