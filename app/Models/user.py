from app import db
class User(db.Model):
    userId = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(60),unique=True,nullable=False)
    password = db.Column(db.String(60),nullable=False)