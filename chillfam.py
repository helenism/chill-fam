from flask import Flask, render_template

app = Flask('chillfam')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/food')
def food():
    return render_template('food.html')

@app.route('/activities')
def activities():
    return render_template('activities.html')

@app.route('/music')
def music():
    return render_template('music.html')

@app.route('/yourfam')
def yourfam():
    return render_template('yourfam.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

app.run(debug=True)
