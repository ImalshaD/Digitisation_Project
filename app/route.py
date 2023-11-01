from app import app
from .Controllers import login_bp,module_bp
app.register_blueprint(login_bp, url_prefix='/auth')
app.register_blueprint(module_bp,url_prefix='/module')
@app.route('/check')
def say_hi():
    return 'Hi, App is up and Running'