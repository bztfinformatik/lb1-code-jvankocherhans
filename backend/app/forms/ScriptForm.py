from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.fields import DecimalField, TextAreaField
from wtforms.validators import InputRequired, Length, ValidationError
from model.models import Script


class ImportScript(FlaskForm):
    scriptName = StringField(validators=[InputRequired()])
    scriptContent = TextAreaField(validators=[InputRequired()])

    submit = SubmitField('Create Script')
