from flask import *
from forms import CalculationForm
from flask_sqlalchemy import SQLAlchemy 
import math

#Configuration
app = Flask(__name__)
app.config.from_object("config.Config")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

#Models
class Entry(db.Model):
	id = db.Column('id', db.Integer, primary_key = True)
	result = db.Column(db.String(200))

	def __init__(self, result):
   		self.result = result

	def __repr__(self):
   		return '<Result %r>' % self.result 

#Routes
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = CalculationForm()
	if form.validate_on_submit():
		result = calculate(form.firstArgument.data, form.operator.data, form.secondArgument.data)
		newEntry = Entry(result)
		db.session.add(newEntry)
		db.session.commit()
		flash('Calculation Successful!')
		return redirect(url_for('index'))
	calculations = Entry.query.all()
	length = len(calculations)
	calculations = calculations[(length-9):]
	return render_template('index.html', title='index', form=form, calculations = calculations) #calculations = db.query...

#Functions
def calculate(arg1:int, op:str, arg2:int):
	result = 0
	if op == '+':
		result = arg1 + arg2
	elif op == '-':
		result = arg1 - arg2
	elif op == '*':
		result = arg1 * arg2
	elif op == '/':
		result = arg1 / arg2
	elif op == '%':
		result = arg1 % arg2
	elif op == 'pow':
		result = math.pow(arg1,arg2)
	elif op == 'log': 
		result = math.log(arg1,arg2)
	return str(arg1)+" "+op+" "+str(arg2)+" = "+str(result)

if __name__== "__main__":
	db.create_all()
	app.run(debug=True)