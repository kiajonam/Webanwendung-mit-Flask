from flask import Blueprint, render_template, request, flash, jsonify
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=1)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    notes = Note.query.filter_by(user_id=1).all()
    return render_template("home.html", notes=notes)

@views.route('/delete_note', methods=['POST'])
def delete_note():
    data = json.loads(request.data)
    note_id = data['noteId']
    note = Note.query.get(note_id)
    if note and note.user_id == 1:
        db.session.delete(note)
        db.session.commit()
        return jsonify({}), 200
    return jsonify({'error': 'Unauthorized or not found'}), 400
