from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# Definições de App ----------------------------------------------------------
app = Flask(__name__)

# -- Vincular ao banco
usuario_db = "root" ; senha_db = "123456" ; banco_db = "bank"
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{usuario_db}:{senha_db}@localhost:3306/{banco_db}'
app.app_context().push()

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'nome-seguro-baby'

# Instâncias -------

# -- Database
db = SQLAlchemy(app)
# -- Flask-Login
lm = LoginManager()
lm.login_view = '/'
lm.init_app(app)
# -- Flask-Bcrypt
by = Bcrypt(app)



