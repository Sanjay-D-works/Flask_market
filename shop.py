from enum import unique

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)



class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(),nullable=False)
    barcode = db.Column(db.String(length=12),nullable=False,unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)

@app.route('/')
@app.route('/Home')
def home_page():
    return render_template('Home.html')

@app.route('/Market')
def market_page():
    item = [
        {'id': 1,'name':'Phone','barcode':'916381008313','price':500},
        {'id': 1, 'name': 'Laptop', 'barcode': '916381001383', 'price': 700},
        {'id': 1, 'name': 'Keyboard', 'barcode': '916381830013', 'price': 800}
    ]
    return render_template('market.html',item=item)