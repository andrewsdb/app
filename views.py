from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Andrew' }
    posts = [
        { 
            'author': { 'nickname': 'Andrew' }, 
            'body': 'Beautiful New York!' 
        },
        { 
            'author': { 'nickname': 'Susan' }, 
            'body': 'Cool!' 
        },
        { 
            'author': { 'nickname': 'Bobby' }, 
            'body': 'Frank Sinatra the best!:)!' 
        }	
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)

@app.route('/lasvegas/')
def currency():
    return render_template("lasvegas.html", title = 'Las Vegas')

@app.route('/panama/')
def quantity():
    return render_template("panama.html", title = 'Panama City')
