# db test
from flask import render_template
from app import app
from app.sql import runSQL

@app.route('/dbtest')
def dbtest():
    rows = runSQL("SELECT * FROM items;")

    return render_template("dbtest.html",
                            title1=app.config['API_NAME'],
                            title2='version {}'.format(app.config['API_VERSION']), items=rows)
