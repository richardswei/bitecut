from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .. import db
#from ..auth.forms import LoginForm

from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user

@main.route('/', methods = ['GET','POST'])
def index():
    return render_template('login.html', current_user = current_user)
