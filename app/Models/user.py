from app import db
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(60),unique=True,nullable=False)
    password = db.Column(db.String(60),nullable=False)
    modules = db.relationship("Module",backref="user",lazy=True)

    def __repr__(self):
        return f"User('{self.user_name}')"