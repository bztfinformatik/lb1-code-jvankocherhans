import os

from flask import Flask
from controllers.user import user_blueprint
from controllers.employee import employee_blueprint
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from model.models import User
from flask_bcrypt import Bcrypt

from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv # Umgebungsvariablen aus dem .env laden
from flask_cors import CORS

# Umgebungsvariablen vom .env File entgegennehmen
load_dotenv() 

app = Flask(__name__)
app.secret_key = "VerySecretSecretKey"

# Applikation als CORS für react definieren
CORS(app)

csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users_blueprint.login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# db.init_app(app)

# hier blueprint registrieren
app.register_blueprint(user_blueprint)

