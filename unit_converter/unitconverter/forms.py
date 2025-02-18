from flask_wtf import FlaskForm
# from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField, SubmitField, BooleanField,SelectField,FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError


class LengthForm(FlaskForm):
    
    choices = [('millimeter', 'millimeter'), ('centimeter', 'centimeter'), ('meter', 'meter'), ('kilometer', 'kilometer'), ('inch', 'inch'), ('foot', 'foot'), ('yard', 'yard'), ('mile', 'mile')]
    
    dropdown = SelectField('Unit to Convert from', choices=choices,validators=[DataRequired()],coerce=str,default='opt1')

    value = FloatField('Input value', validators=[DataRequired()])

    dropdown_2 = SelectField('Unit to Convert to', choices=choices,validators=[DataRequired()],coerce=str,default='opt1')
 
    submit = SubmitField('Convert')



class WeightForm(FlaskForm):

    choices = [('milligram', 'milligram'), ('gram', 'gram'), ('kilogram', 'kilogram'), ('ounce', 'ounce'), ('pound', 'pound')]

    dropdown = SelectField('Unit to Convert from', choices=choices,validators=[DataRequired()],coerce=str,default='opt1')

    value = FloatField('Input value', validators=[DataRequired()])

    dropdown_2 = SelectField('Unit to Convert to', choices=choices,validators=[DataRequired()],coerce=str,default='opt1')

    submit = SubmitField('Convert')


class TemperatureForm(FlaskForm):

    choices = [('celsius', 'Celsius'), ('fahrenheit', 'Fahrenheit'), ('kelvin', 'Kelvin')]

    dropdown = SelectField('Unit to Convert from', choices=choices,validators=[DataRequired()],coerce=str,default='opt1')

    value = FloatField('Input value', validators=[DataRequired()])

    dropdown_2 = SelectField('Unit to Convert to', choices=choices,validators=[DataRequired()],coerce=str,default='opt1')

    submit = SubmitField('Convert')
