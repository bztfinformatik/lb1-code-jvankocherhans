import sqlalchemy
import sqlalchemy.orm

from flask import redirect, request, flash
from flask.templating import render_template
from flask import Blueprint
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from forms.ScriptForm import ImportScript
from model.models import Script, db

script_blueprint = Blueprint('script_blueprint', __name__)


@script_blueprint.route("/logedin/importScript", methods=["GET", "POST"])
@login_required
def importScript():
    # Aufbau der DB Session
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    # Initialisierung des Formulars
    addScriptForm = ImportScript()

    # Bei Post-Method soll Script mit den Angaben in der Datenbank gepsichert werden
    if request.method == 'POST':
        if addScriptForm.validate_on_submit():
            new_Script = Script(scriptID=None, scriptName=addScriptForm.scriptName.data, scriptContent=addScriptForm.scriptContent.data)

            db.session.add(new_Script)
            db.session.commit()

            # Redirect zur Anzeige mit allen Scripts
            return redirect("/logedin/runScript")

    return render_template("/logedin/importScript.html", form=addScriptForm)



@script_blueprint.route("/logedin/runScript")
@login_required
def showScript():
        # workaround für sesssion Autocomplete
    session: sqlalchemy.orm.Session = db.session

    # alle swicthes laden
    scripts = session.query(Script).order_by(Script.scriptID).all()

    return render_template("logedin/runScript.html", scripts=scripts)
