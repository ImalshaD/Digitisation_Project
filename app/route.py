from app import app
from .Controllers import login_bp,module_bp,moduleYear_bp,marksheet_bp
app.register_blueprint(login_bp, url_prefix='/auth')
app.register_blueprint(module_bp,url_prefix='/module')
app.register_blueprint(moduleYear_bp,url_prefix="/moduleYear")
app.register_blueprint(marksheet_bp,url_prefix="/marksheet")
@app.route('/check')
def say_hi():
    return 'Hi, App is up and Running'