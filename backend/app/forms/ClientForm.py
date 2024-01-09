from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, validators
from wtforms.fields import DecimalField, TextAreaField
from wtforms.validators import InputRequired, Length, ValidationError, Regexp
from model.models import Client


class ImportClient(FlaskForm):
    mac = StringField('MAC Address', [
        InputRequired(),
        Regexp(
            # Regex for valid MAC-Address
            regex=r'^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$',
            message='Invalid MAC address format. Please use XX:XX:XX:XX:XX:XX'
        )])
    
    hostname = StringField('Hostname', validators=[InputRequired(),
        Regexp(
            # Regex for valid Hostname -> Alphanumeric, Hyphens and Dots allowed
            regex=r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.[A-Za-z0-9-]{1,63})*$',
            message='Invalid Hostname address format. Please use alphanumeric characters and hyphens.'
        )])
    submit = SubmitField('Trust Client')