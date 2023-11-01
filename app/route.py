from app import app
from .Controllers import login_bp
app.register_blueprint(login_bp, url_prefix='/auth')
@app.route('/check')
def say_hi():
    return 'Hi, App is up and Running'