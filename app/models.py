from . import db
from datetime import datetime

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(255), index=True)
    pitches=db.relationship('Pitch', backref= 'category', lazy='dynamic')
    
    def save_category(self):
        db.session.add(self)
        db.session.commit()
    


class Pitch(db.Model):
    __tablename__ = 'pitch'
    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(255))
    content = db.Column(db.String(255))
    category_id = db.Column(db.Integer,db.ForeignKey("category.id"))
    posted = db.Column(db.DateTime,default=datetime.utcnow)


    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls):
        pitches = Pitch.query.all()
        return pitches
