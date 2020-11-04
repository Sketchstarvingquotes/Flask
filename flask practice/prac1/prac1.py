from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def hello():

    return render_template('index.html')

@app.route("/about")
def sumit():
    name = "Sumit Sudalkar"
    return render_template('about.html', name= name)
app.run(debug=True)