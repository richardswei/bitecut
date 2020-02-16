from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin, AnonymousUserMixin
from . import db
from datetime import datetime
from datetime import date

class Provider(db.Model):
    __tablename__ = 'provider'
    name = db.Column(db.String(64))
    email = db.Column(db.String(64), unique = True, primary_key = True)
    password = db.Column(db.String(128))
    address = db.Column(db.String(128))
    coords_x = db.Column(db.Float)
    coords_y = db.Column(db.Float)
    lists = db.relationship('Listing', backref='provider', lazy=True)

class Customer(db.Model):
    __tablename__ = 'customer'
    name = db.Column(db.String(64))
    email = db.Column(db.String(64), unique = True, primary_key = True)
    password = db.Column(db.String(128))
    reserves = db.relationship('Reservation', backref='customer', lazy=True)

class Listing(db.Model):
    __tablename__ = 'listing'
    listing_ID = db.Column(db.Integer, primary_key = True, autoincrement = True)
    provider_email = db.Column(db.String(64), db.ForeignKey('provider.email'), nullable = False)
    dish = db.Column(db.String(64))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    type = db.Column(db.String(64))


class Reservation(db.Model):
    __tablename__ = 'reservation'
    customer_email = db.Column(db.String(64), db.ForeignKey('customer.email'), nullable = False)
    res_ID = db.Column(db.Integer, primary_key = True, autoincrement = True)
    listing_ID = db.Column(db.Integer, db.ForeignKey('listing.listing_ID'), primary_key = True)
