from flask import render_template, redirect, request, url_for
from scoreboard import app
from scoreboard.forms import AddPlayerForm, ChoosePlayerForm, SaveGame
from scoreboard.models import users, results
from scoreboard import db


@app.route('/', methods=['GET', 'POST'])
def home():
    form2 = ChoosePlayerForm(request.form)
    # print("player1: " + request.form['score1'])
    # print("player2: " + request.form['score2'])
    if request.method == "POST" and form2.validate():
        print("der geht")
        score = results(player1='hjk',
                        player2='gatz',
                        goals1=request.form['score1'],
                        goals2=request.form['score2'],
                        date='01.01.2001')

        if not score.goals1 and not score.goals2:
            score.goals1 = 0
            score.goals2 = 0
        elif not score.goals1:
            score.goals1 = 0
        elif not score.goals2:
            score.goals2 = 0


        db.session.add(score)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        print("Irgendein Quatsch geschieht (oben)")

    return render_template('home.html', form2=form2)


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


