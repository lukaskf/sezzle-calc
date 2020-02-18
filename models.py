from run import db

class Entry(db.model):
	id = db.Column('id', db.Intger, primary_key = True)
	result = db.Column(db.String(200))