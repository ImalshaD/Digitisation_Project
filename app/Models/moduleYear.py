from app import db
class ModuleYear(db.Model):
    module_year_id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer,nullable=False)
    caweights = db.Column(db.Float,nullable=False)
    finalweights = db.Column(db.Float,nullable=False)
    camax = db.Column(db.Float,nullable=False)
    finalmax = db.Column(db.Float,nullable=False)
    moderated = db.Column(db.Boolean,nullable=False,default=False)
    module_id = db.Column(db.Integer, db.ForeignKey('module.module_id'), nullable=False)
    max_qs = db.Column(db.Integer,nullable=False)
    marks = db.relationship("Marks",backref="moduleYear",lazy=True)

    def __repr__(self):
        return f"Module('{self.module_id}, {self.year}')"