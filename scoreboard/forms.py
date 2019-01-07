from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, InputRequired
from wtforms_sqlalchemy.fields import QuerySelectField
from scoreboard.models import users


class AddPlayerForm(FlaskForm):
    Name = StringField('Name', validators=[DataRequired()])
    Color = SelectField(u'Farbe', choices=[('#FF0000', 'Rot'),
                                           ('#00FF00', 'Gruen'),
                                           ('#0000FF', 'Blau'),
                                           ('#FFFF00', 'Gelb'),
                                           ('#FF00FF', 'Magenta'),
                                           ('#808080', 'Grau'),
                                           ('#000000', 'Schwarz'),
                                           ('#FFFFFF', 'Weiss'),
                                           ('#FF8C00', 'Orange'),
                                           ('#00FFFF', 'Cyan')])
    submit = SubmitField('Speichern')


def users_query():
    return users.query


class ChoosePlayerForm(FlaskForm):
    Player = QuerySelectField(query_factory=users_query, allow_blank=False)
    submit = SubmitField('Spiel speichern!')

class SaveGame(FlaskForm):
    submit = SubmitField('Spiel speichern!')
