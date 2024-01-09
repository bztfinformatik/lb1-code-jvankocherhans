from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError, Regexp
from model.models import Switch


class ImportSwitch(FlaskForm):
    
    hostname = StringField('Hostname', validators=[
        InputRequired(),
        Regexp(
            # Regex for valid Hostname -> Alphanumeric, Hyphens and Dots allowed
            regex=r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.[A-Za-z0-9-]{1,63})*$',
            message='Invalid Hostname address format. Please use alphanumeric characters and hyphens.'
    )])
    
    ip = StringField(validators=[
        InputRequired(),
          Regexp(
            # Regex for valid Hostname -> Alphanumeric, Hyphens and Dots allowed
            regex=r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b',
            message='Invalid IP address format. Please use numbers Seperated by Dots: 0.0.0.0.'
        )    
    ])
    switchType = StringField(validators=[InputRequired()])

    submit = SubmitField('Create')
