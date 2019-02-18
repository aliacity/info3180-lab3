from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class ContactForm (FlaskForm):
    name = TextField('Name',validators=[DataRequired()])
    email = TextField('Email address', validators=[DataRequired(), Email()])
    subject = TextField ('Subject of Message')
    textarea = TextAreaField ('Body of message', validators=[DataRequired()])
    send = SubmitField('Send')