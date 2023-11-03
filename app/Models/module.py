from app import db
class Module(db.Model):
    module_id = db.Column(db.Integer, primary_key=True)
    module_code = db.Column(db.String(60), unique=True,nullable=True)
    module_name = db.Column(db.String(60), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    module_years = db.relationship("ModuleYear",backref="module",lazy=True)

    
    def __repr__(self):
        return f"Module('{self.module_name}')"