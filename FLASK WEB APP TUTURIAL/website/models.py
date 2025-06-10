from . import db
from flask_login import UserMixin
from datetime import datetime

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer)  # ساده برای نمونه
