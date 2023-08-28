from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///comunidade.db"
app.config['SECRET_KEY'] = 'abbbb114a4d2644a86af9f5f56ae49d1'
app.config['UPLOAD_FOLDER'] = "static/fotos_posts"
database = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'homepage'


from fakepinterest import routes
