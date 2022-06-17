from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class RegistrationForm(FlaskForm):
    customername = StringField('Customer Name', validators=[DataRequired()])
    roadmap = StringField('Roadmap Type', validators=[DataRequired()])
    submit = SubmitField('Generate Survey')
