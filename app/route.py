from app import app

@app.route('/check')
def say_hi():
    return 'Hi, App is up and Running'