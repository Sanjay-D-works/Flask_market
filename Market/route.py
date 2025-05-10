from Market import app
from flask import render_template
from Market.models import Item
from Market.forms import RegisterFrom

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@app.route('/register')
def register_page():
    form = RegisterFrom()
    return render_template('register.html',form=form)