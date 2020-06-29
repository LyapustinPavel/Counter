from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileAllowed, FileField
import os

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    file = FileField('Text file', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    submit = SubmitField('ПЕРЕДАТЬ')
