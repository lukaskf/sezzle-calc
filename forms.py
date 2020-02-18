from flask_wtf import *
from wtforms import *
from wtforms.validators import DataRequired, Regexp, AnyOf

#operations: + , -, * / , % , pow , swrt 
class CalculationForm(FlaskForm):
	firstArgument = IntegerField('First Argument', validators=[DataRequired()]) #Regexp('^(\+|-)?\d+$')
	operator = StringField('Operator', validators=[DataRequired(), 
		AnyOf(['+', '-', '*', '/', '%', 'pow', 'log'])])
	secondArgument = IntegerField('Second Argument', validators=[DataRequired()])  #Regexp('^(\+|-)?\d+$')
	submit = SubmitField('Calculate')