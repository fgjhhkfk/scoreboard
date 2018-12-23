from flask import render_template, redirect, request, url_for
from scoreboard import app
from scoreboard.forms import AddPlayerForm, ChoosePlayerForm
from scoreboard.models import users, results
from scoreboard import db


@app.route('/', methods=['GET', 'POST'])
def home():
    form = ChoosePlayerForm()
    return render_template('home.html', form=form)


@app.route('/test')
def test():
    form = AddPlayerForm()
    return render_template('test.html', form=form)


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


@app.route('/', methods=['GET', 'POST'])
def save_game():
    # form = SaveGame()
    form = ChoosePlayerForm()
    print("player1: " + request.form['score1'])
    print("player2: " + request.form['score2'])
    if form.validate_on_submit():
        print("der geht")
        score = results(player1='hjk',
                        player2='gatz',
                        goals1=request.form['score1'],
                        goals2=request.form['score2'],
                        date='01.01.2001')
        db.session.add(score)
        db.session.commit()
        return redirect(url_for('/'))
    else:
        print("Irgendein Quatsch geschieht")

    return render_template('home.html', form=form)
