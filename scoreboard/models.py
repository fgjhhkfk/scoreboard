from scoreboard import db


class users(db.Model):
    __tablenames__ = 'users'
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    color = db.Column(db.String)

    def __repr__(self):
        return "{}".format(self.username)


class results(db.Model):
    __searchable__ = []
    __tablename__ = 'scores'
    gameid = db.Column(db.Integer, primary_key=True)
    player1 = db.Column(db.String)
    player2 = db.Column(db.String)
    goals1 = db.Column(db.String)
    goals2 = db.Column(db.String)
    date = db.Column(db.BLOB)
