from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, Length

class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age of Pet", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes About Pet")

class EditPetForm(FlaskForm):
    photo = StringField('Update Photo URL', validators=[Optional(), URL()])
    notes = TextAreaField('Notes About Pet', validators=[Length(min=10), Optional()])
    available = BooleanField('Available')