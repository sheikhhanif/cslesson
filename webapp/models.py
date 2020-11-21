from datetime import datetime
from webapp import db
from flask_login import UserMixin

class Video(db.Model, UserMixin):
    vid = db.Column(db.String(150), primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    thumbnail = db.Column(db.String(200), nullable=False)
    channel = db.Column(db.String(100), nullable=False)
    tag = db.Column(db.String(50), nullable=False)

    def __repr__(self):
            return f"Video('{self.vid}', '{self.title}','{self.category}', '{self.thumbnail}','{self.channel}','{self.tag}')"