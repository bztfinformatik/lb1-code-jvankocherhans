import sqlalchemy
import sqlalchemy.orm

from flask import redirect, request, flash
from flask.templating import render_template
from flask import Blueprint
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from forms.SwitchForm import ImportSwitch
from model.models import Log, db

from controllers.decorater import requires_access_level
from model.ACCESS import ACCESS


showReactions_blueprint = Blueprint('showReactions_blueprint', __name__)


@showReactions_blueprint.route("/logedin/showReactions")
@requires_access_level(ACCESS['user'])
def showPage():
    # workaround für sesssion Autocomplete
    session: sqlalchemy.orm.Session = db.session

    # alle swicthes laden
    logs = session.query(Log).order_by(Log.date).all()

    return render_template("logedin/showReactions.html", logs=logs)
