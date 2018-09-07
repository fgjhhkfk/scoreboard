# import os
# from flask import Flask, render_template, request, url_for, redirect, flash
from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import AddPlayerForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scoreboard.sqlite'
app.config['SECRET_KEY'] = '1234567890'

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
    date = db.Column(db.BLOB)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/add_player', methods=['GET', 'POST'])
def add_player():
    form = AddPlayerForm()
    if form.validate_on_submit():
        user = users(username=form.Name.data,
                     color=form.Color.data)

        db.session.add(user)
        db.session.commit()
        return redirect('/')

    return render_template('add_player.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
