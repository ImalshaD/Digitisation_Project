from app import app
from .Controllers import login_bp,module_bp,moduleYear_bp,marksheet_bp,ca_bp,ds_bp
app.register_blueprint(login_bp, url_prefix='/auth')
app.register_blueprint(module_bp,url_prefix='/module')
app.register_blueprint(moduleYear_bp,url_prefix="/moduleYear")
app.register_blueprint(marksheet_bp,url_prefix="/marksheet")
app.register_blueprint(ca_bp,url_prefix="/ca")
app.register_blueprint(ds_bp,url_prefix="/ds")
@app.route('/check')
def say_hi():
    return 'Hi, App is up and Running'