

from flask import redirect, request, flash, url_for
from flask.templating import render_template
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask import Blueprint
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()

user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route("/login", methods=["GET", "POST"])
def login():

    return "test"


# @user_blueprint.route("/dashboard", methods=["GET", "POST"])
# @login_required
# def dashboard():
#     return render_template('dashboard.html')

# @user_blueprint.route("/logout", methods=["GET", "POST"])
# @login_required
# def logout():
#     logout_user()
#     return redirect('/login')


# @user_blueprint.route("/register", methods=["GET", "POST"])
# def register():

#     return render_template('register.html', form=form)
