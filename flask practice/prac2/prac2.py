from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ragister')
def ragister():
    return render_template('ragister.html')

@app.route('/thankyou')
def thankyou():
    first = request.args.get('first')
    last = request.args.get('last')
    email = request.args.get('email')
    password = request.args.get('password')
    return render_template('thankyou.html', first=first, last=last, email=email, password=password)

if __name__ == "__main__":
    app.run(debug = True)
