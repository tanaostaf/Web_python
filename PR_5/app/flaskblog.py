from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
#from forms import RegistrationForm, LoginForm
#basedir = os.path.abspath(os.path.dirname(__file__))

app  = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#+ os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default = 'default.jpg')
	password = db.Column(db.String(60), nullable = False)
	posts = db.relationship('Post', backref='author', lazy=True)
	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
	content = db.Column(db.Text, nullable=False)	
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable = False)
	
	def __repr__(self):
		return f"Post('{self.title}', '{self.date_posted}')"		