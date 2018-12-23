from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scoreboard.sqlite'
app.config['SECRET_KEY'] = '1234567890'

db = SQLAlchemy(app)

from scoreboard import routes
