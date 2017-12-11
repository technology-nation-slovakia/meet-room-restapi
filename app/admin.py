# Admin module
from flask import render_template
from app import app

@app.route('/')
@app.route('/index.html')
def index():
    return render_template("index.html",
                            title1=app.config['API_NAME'],
                            title2='version {}'.format(app.config['API_VERSION']))

@app.route('/admin')
def admin():
    return render_template("admin.html",
                            title1='{} | version {}'.format(app.config['API_NAME'], app.config['API_VERSION']),
                            title2='Admin Panel')
