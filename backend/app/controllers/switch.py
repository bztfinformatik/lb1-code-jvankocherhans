import sqlalchemy
import sqlalchemy.orm

from flask import redirect, request, flash
from flask.templating import render_template
from flask import Blueprint
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from forms.SwitchForm import ImportSwitch
from model.models import Switch, db

from controllers.decorater import requires_access_level
from model.ACCESS import ACCESS


switch_blueprint = Blueprint('switch_blueprint', __name__)

@switch_blueprint.route("/logedin/importSwitch",  methods=["GET", "POST"])
@requires_access_level(ACCESS['admin'])
def importSwitch():
    # Aufbau der Session
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    # Initialisierung des Formulars
    addSwitchForm = ImportSwitch()

    # Bei Post-Method soll der Switch mit den ANgaben in der Datenbank gepsichert werden
    if request.method == 'POST':
        if addSwitchForm.validate_on_submit():
            new_Switch = Switch(hostname=addSwitchForm.hostname.data, ip=addSwitchForm.ip.data, switchType=addSwitchForm.switchType.data)

            db.session.add(new_Switch)
            db.session.commit()

            return redirect("/logedin/showSwitches")

    return render_template("/logedin/importSwitch.html", form=addSwitchForm)


@switch_blueprint.route("/logedin/showSwitches")
@requires_access_level(ACCESS['user'])
def showSwitches():
    # workaround für sesssion Autocomplete
    session: sqlalchemy.orm.Session = db.session

    # alle swicthes laden
    switches = session.query(Switch).order_by(Switch.hostname).all()

    return render_template("logedin/showSwitches.html", switches=switches)


@switch_blueprint.route("/logedin/deleteSwitch/<hostname>")
@requires_access_level(ACCESS['user'])
def deleteSwitche(hostname):
    # workaround für sesssion Autocomplete
    session: sqlalchemy.orm.Session = db.session
    # Nach Switch Filter mit dem bestimmten Hostname
    switchToDelete = db.session.query(Switch).filter(Switch.hostname == hostname)
    # gefunden Switch entfernen
    switchToDelete.delete()
    # DB Commit
    db.session.commit()

    return redirect("/logedin/showSwitches")

