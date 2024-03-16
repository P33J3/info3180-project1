from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Regexp
from flask_wtf.file import FileField, FileRequired, FileAllowed


class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[
        InputRequired(message='Required'),
        Regexp(r'^[a-zA-Z0-9-:.!%\s]+$', message='Invalid Characters Used')
    ])

    bedrooms = StringField('No. of Rooms', validators=[
        InputRequired(message='Required'),
        Regexp('^\\d+$', message='Invalid Characters Used')
    ])

    bathrooms = StringField('No. of Bathrooms', validators=[
        InputRequired(message='Required'),
        Regexp(r'^\d*[.,]?\d*$', message='Invalid Characters Used')
    ])

    location = StringField('Location', validators=[
        InputRequired(message='Required'),
        Regexp(r'^[a-zA-Z0-9-:.!%\s]+$', message='Invalid Characters Used')
    ])

    price = StringField('Price', validators=[
        InputRequired(message='Required'),
        Regexp(r'^\d*[.,]?\d*$', message='Invalid Characters Used')
    ])

    type = SelectField('Property Type', choices=[
        ('House', 'House'), ('Apartment', 'Apartment')],
                       validators=[
                           InputRequired(message='Input Required')])

    description = TextAreaField('Description', validators=[
        InputRequired(message='Required'),
        Regexp(r'^[a-zA-Z0-9-:.!%\s]+$', message='Invalid Characters Used')
    ])

    photo = FileField('Photo', validators=[
        FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')
    ])
