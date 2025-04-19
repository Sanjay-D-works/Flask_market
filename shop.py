from flask import Flask, render_template
app = Flask(__name__)

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
    return render_template('market.html',item=item)  #returns