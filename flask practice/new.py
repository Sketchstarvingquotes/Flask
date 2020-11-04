from flask import Flask, url_for, redirect

app = Flask (__name__)

@app.route('/')
def index():
    return "The index"

@app.route('/first')
def first_router():
    return url_for('index')

if __name__ == '__main__':
    app.run(debug = True)