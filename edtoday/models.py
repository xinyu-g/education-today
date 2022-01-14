from . import db

class Task1(db.Model):
    paperId = db.Column(db.Integer, primary_key=True)
    refCount = db.Column(db.Integer)
    citedBy = db.Column(db.Integer)



class Task2(db.Model):
    