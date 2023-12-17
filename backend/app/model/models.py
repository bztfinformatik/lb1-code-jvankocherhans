# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from model.ACCESS import ACCESS


db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    access = db.Column(db.SmallInteger, nullable=False, default=0)

    def is_admin(self):
        return self.access == ACCESS['admin']

    def is_user(self):
        return self.access == ACCESS['user']

    def allowed(self, access_level):
        return self.access >= access_level
    

class Switch(db.Model):
    __tablename__ = 'switch'

    hostname = db.Column(db.String(50), primary_key=True)
    ip = db.Column(db.String(16), nullable=False)
    switchType = db.Column(db.String(50))

class Client(db.Model):
    __tablename__ = 'client'

    mac = db.Column(db.String(18), primary_key=True)
    hostname = db.Column(db.String(50), nullable=False)


class Script(db.Model):
    __tablename__ = 'script'

    scriptID = db.Column(db.Integer, primary_key=True)
    scriptName = db.Column(db.String(50), nullable=False)
    scriptContent = db.Column(db.String(500), nullable=False)

class Log(db.Model):
    __tablename__ = 'log'

    logEvent = db.Column(db.Integer, nullable=False, primary_key=True)
    date = db.Column(db.Date, nullable=False)
