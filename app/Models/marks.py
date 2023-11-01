from app import db

class Marks(db.Model):
    index_number = db.Column(db.String(20),primary_key = True)
    module_year_id = db.Column(db.ForeignKey('module_year.module_year_id'), nullable=False)
    q1 = db.Column(db.Float,nullable=True)
    q2 = db.Column(db.Float,nullable=True)
    q3 = db.Column(db.Float,nullable=True)
    q4 = db.Column(db.Float,nullable=True)
    q5 = db.Column(db.Float,nullable=True)
    q6 = db.Column(db.Float,nullable=True)
    q7 = db.Column(db.Float,nullable=True)
    q8 = db.Column(db.Float,nullable=True)
    q9 = db.Column(db.Float,nullable=True)
    q10 = db.Column(db.Float,nullable=True)
    q11 = db.Column(db.Float,nullable=True)
    q12 = db.Column(db.Float,nullable=True)
    final = db.Column(db.Float,nullable=True)
    moderated_final = db.Column(db.Float,nullable=True)

