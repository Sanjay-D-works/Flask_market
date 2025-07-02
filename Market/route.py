from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

from Market import app
from flask import render_template, redirect, url_for
from Market.models import Item, User
from Market.forms import RegisterForm
from Market import db



@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

#Cross Site Request Forgery(CSRF)
@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password_hash=generate_password_hash(form.password1.data))
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}: # IF there are not errors from the validations
        for err_msg in form.errors.values():
            print(f'There was an error with creating a user: {err_msg}')
    return render_template('register.html', form=form)