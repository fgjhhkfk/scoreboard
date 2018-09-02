# import os
# from flask import Flask, render_template, request, url_for, redirect, flash
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scoreboard.sqlite'

db = SQLAlchemy(app)


class users(db.Model):
    __tablenames__ = 'users'
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    color = db.Column(db.String)


class results(db.Model):
    __searchable__ = []
    __tablename__ = 'scores'
    gameid = db.Column(db.Integer, primary_key=True)
    player1 = db.Column(db.String)
    player2 = db.Column(db.String)
    goals1 = db.Column(db.String)
    goals2 = db.Column(db.String)
    date = db.Column(BLOB)



@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
