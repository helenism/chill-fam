from flask import Flask, render_template

app = Flask('chillfam')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/yourfam')
def yourfam():
    return render_template('yourfam.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

app.run(debug=True)
