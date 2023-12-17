from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.fields import DecimalField, TextAreaField
from wtforms.validators import InputRequired, Length, ValidationError
from model.models import Client


class ImportClient(FlaskForm):
    mac = StringField(validators=[InputRequired()])
    hostname = StringField(validators=[InputRequired()])

    submit = SubmitField('Trust Client')
