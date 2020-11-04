import datetime
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def index():
    current_dt = datetime.datetime.now()
    return render_template('index.html', current_dt = current_dt)

app.run()