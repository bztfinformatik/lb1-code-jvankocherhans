import sqlalchemy
import sqlalchemy.orm

from flask import redirect, request, flash
from flask.templating import render_template
from flask import Blueprint
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from forms.ClientForm import ImportClient
from model.models import Client, db


client_blueprint = Blueprint('client_blueprint', __name__)


@client_blueprint.route("/logedin/importClient", methods=["GET", "POST"])
@login_required
def importClient():
    
    # Aufbau der DB Session
    session: sqlalchemy.orm.scoping.scoped_session = db.session

    # Initialisierung des Formulars
    addClientForm = ImportClient()

    # Bei Post-Method soll Client mit den Angaben in der Datenbank gesichert werden
    if request.method == 'POST':
        if addClientForm.validate_on_submit():
            new_Client = Client(mac=addClientForm.mac.data, hostname=addClientForm.hostname.data)

            db.session.add(new_Client)
            db.session.commit()

            # Redirect zur Anzeige mit allen trusted Clients
            return redirect("/logedin/runScript")
   
    return render_template("/logedin/importClient.html", form=addClientForm)
