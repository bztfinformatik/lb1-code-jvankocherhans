from flask import redirect, request, flash
from flask.templating import render_template
from flask import Blueprint
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user


importClient_blueprint = Blueprint('importClient_blueprint', __name__)


@importClient_blueprint.route("/logedin/importClient")
@login_required
def showPage():
    return render_template("logedin/importClient.html")
