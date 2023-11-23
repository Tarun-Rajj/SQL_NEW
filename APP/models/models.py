from sqlalchemy import Column,String
# from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

from sqlalchemy.orm import DeclarativeBase

from APP import db

class Base(DeclarativeBase):
    pass

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    role = db.relationship('Role', backref=db.backref('users', lazy=True))

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='Pending')
    assigned_to = db.Column(db.Integer, db.ForeignKey('user.id'))
    assigned_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    assigned_to_user = db.relationship('User', foreign_keys=[assigned_to], backref='tasks_assigned_to', lazy=True)
    assigned_by_user = db.relationship('User', foreign_keys=[assigned_by], backref='tasks_assigned_by', lazy=True)
