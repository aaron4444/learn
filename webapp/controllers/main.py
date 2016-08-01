import datetime
from os import path
from sqlalchemy import func
from flask import render_template, Blueprint, redirect, url_for, flash, request, session, abort

#from webapp.models import db, Post, Tag, Comment, User, tags, Recipie
#from webapp.forms import CommentForm, RegisterForm, LoginForm, RecipieForm
#from webapp.extensions import facebook, login_manager, admin_permission, poster_permission
from flask_login import login_required, login_user, logout_user, current_user, current_app
from flask_principal import Identity, AnonymousIdentity, identity_changed, Permission, UserNeed

from werkzeug import secure_filename


main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder = '../templates/main'
    )

@main_blueprint.route('/index')
def home():
    return render_template('main/base.html')

@main_blueprint.route('/times')


def times():
    return render_template('main/halachiktimes.html')

@main_blueprint.route('/recipies',  methods=["GET","POST"])

def recipie():
    
    return render_template('main/recipie.html')

@main_blueprint.route('/popup')
def breaks():
    return render_template('main/about_take_breaks.html')


@main_blueprint.route('/facebook')
def facebook_login():
    return facebook.authorize(
        callback=url_for(
            '.facebook_authorized',
            next=request.referrer or None,
            _external=True
        )
    )
