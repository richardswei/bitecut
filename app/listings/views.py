from flask import render_template, redirect, request, url_for, flash, make_response, jsonify
from . import listings
from flask_login import login_user, login_required, logout_user, current_user
from ..models import Provider, Customer, Listing, Reservation
from ..email import send_email
from ..decorators import token_required
from .. import db
from config import config
import re
from functools import wraps
import jwt
import datetime
import app
from ..decorators import token_required

@listings.route('/list', methods = ['GET', 'POST'])
@token_required
def list():
    listing_data = request.get_json(force = True)
    token = request.headers.get('Authorization')
    try:
        data = jwt.decode(token, '1234')
    except:
        return 'didnt work', 403

    print(listing_data)

    new_listing = Listing(provider_email = data['email'], dish = listing_data['dish'], price = listing_data['price'], quantity = listing_data['quantity'], \
                    type = listing_data['type'])
    db.session.add(new_listing)
    db.session.commit()

    return 'worked', 203

@listings.route('/reserve', methods = ['GET', 'POST'])
@token_required
def reserve():
    res_data = request.get_json(force = True)
    token = request.headers.get('Authorization')
    try:
        data = jwt.decode(token, '1234')
    except:
        return 'didnt work', 403

    listing = Listing.query.filter_by(listing_ID=res_data['listing_ID']).first()
    if listing.quantity == 0:
        return 'no supply', 403

    new_res = Reservation(customer_email = data['email'], listing_ID = res_data['listing_ID'])
    db.session.add(new_res)

    listing.quantity -= 1

    db.session.commit()
    return 'worked', 203
