from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'b400e58b4acf076b17c5227e'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from Market import models  # import your models after db is defined
from Market import route
