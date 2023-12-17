from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from model.models import Switch


class ImportSwitch(FlaskForm):
    hostname = StringField(validators=[InputRequired()])
    ip = StringField(validators=[InputRequired()])
    switchType = StringField(validators=[InputRequired()])

    submit = SubmitField('Create')
