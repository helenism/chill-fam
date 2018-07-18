from flask import Flask, render_template

app = Flask('chillfam')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/findyourfam')
def findyourfam():
    return render_template('findyourfam.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

app.run(debug=True)
