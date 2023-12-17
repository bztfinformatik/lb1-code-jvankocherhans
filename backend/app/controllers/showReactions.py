from flask import redirect, request, flash
from flask.templating import render_template
from flask import Blueprint
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user


showReactions_blueprint = Blueprint('showReactions_blueprint', __name__)


@showReactions_blueprint.route("/logedin/showReactions")
@login_required
def showPage():
    return render_template("logedin/showReactions.html")
