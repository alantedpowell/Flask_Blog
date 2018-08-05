from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '53ab42b09ba9d0c81d262156e15f4b44e14bf6ecf32aef6ba387b96911736ba1'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:site.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
#Consider learning about environment variables MacBook should be able to handle it better
app.config['MAIL_USERNAME'] = 'alantep11@gmail.com'
app.config['MAIL_PASSWORD'] = 'Jesus151515!)'
mail = Mail(app)
from flaskblog import routes
