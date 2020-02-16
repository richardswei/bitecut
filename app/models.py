from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin, AnonymousUserMixin
from . import db
from datetime import datetime
from datetime import date

class Provider(db.Model):
    __tablename__ = 'provider'
    email = db.Column(db.String(64), unique = True, primary_key = True)
    password = db.Column(db.String(128))
    posts = db.relationship('listing', backref = 'provider', lazy = True)

class Customer(db.Model):
    __tablename__ = 'customer'
    email = db.Column(db.String(64), unique = True, primary_key = True)
    password = db.Column(db.String(128))
    reserves = db.relationship('reservation', backref = 'customer', lazy = True)

class Listing(db.Model):
    __tablename__ = 'listing'
    listing_ID = db.Column(db.Integer, primary_key = True, autoincrement = True)
    provider_email = db.Column(db.String(64), db.ForeignKey('provider.email'))
    dish = db.Column(db.String(64))
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    type = db.Column(db.String(64))

class Reservation(db.Model):
    __tablename__ = 'reservation'
    res_ID = db.Column(db.Integer, primary_key = True, autoincrement = True)
    listing_ID = db.Column(db.Integer, db.ForeignKey('listing.listing_ID'), primary_key = True)
