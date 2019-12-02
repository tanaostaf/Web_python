from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_admin import Admin
import os


app  = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'site.db')

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
manager = Manager(app)
manager.add_command('db', MigrateCommand)

import flaskblog.forms as views
admin = Admin(app)
#admin.add_view(routes.HelloView(name='Hello'))

from flask_admin.contrib.sqla import ModelView
#import flaskblog.forms as views, UserAdminView
#admin.add_view(ModelView(views.User, db.session))
admin.add_view(views.UserAdminView(views.User, db.session))



from flaskblog import routes
