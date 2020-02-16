from flask import render_template, redirect, request, url_for, flash, make_response, jsonify
from . import auth
from flask_login import login_user, login_required, logout_user, current_user
from ..models import Provider, Customer
from ..email import send_email
from ..decorators import token_required
from .. import db
from config import config
import re
from functools import wraps
import jwt
import datetime
import app


@auth.route('/provider/register', methods = ['GET', 'POST'])
def register_provider():
    provider_data = request.get_json(force = True)
    new_provider = Provider(name = provider_data['name'], email = provider_data['email'], password = provider_data['password'], \
                   address = provider_data['address'], coords_x = provider_data['coords_x'], coords_y = provider_data['coords_y'])
    db.session.add(new_provider)
    db.session.commit()
    return 'provider registered successfully', 200

@auth.route('/customer/register', methods = ['GET', 'POST'])
def register_customer():
    customer_data = request.get_json(force = True)
    new_customer = Customer(name = customer_data['name'], email = customer_data['email'], password = customer_data['password'])
    db.session.add(new_customer)
    db.session.commit()
    return 'customer registered successfully', 200

@auth.route('/provider/login', methods = ['GET', 'POST'])
def authenticate_provider():
    login_data = request.get_json()
    print(login_data)
    user = Provider.query.filter_by(email=login_data['email']).first()
    if login_data and login_data['password'] == user.password:
        token = jwt.encode({'email': login_data['email'], 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes = 300)}, '1234')
        return jsonify({'token' : token.decode('UTF-8')})
    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm = "Login Required"'})

@auth.route('/customer/login', methods = ['GET', 'POST'])
def authenticate_customer():
    login_data = request.get_json()
    user = Customer.query.filter_by(email=login_data['email']).first()
    if login_data and login_data['password'] == user.password:
        token = jwt.encode({'email': login_data['email'], 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes = 30)}, '1234')
        return jsonify({'token' : token.decode('UTF-8')})
    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm = "Login Required"'})
