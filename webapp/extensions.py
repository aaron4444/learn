from flask_bcrypt import Bcrypt
from flask import session
from flask_login import LoginManager
from flask_uploads import UploadSet, IMAGES
from flask_principal import Principal, Permission, RoleNeed
from flask_restful import Api


bcrypt= Bcrypt()
login_manager = LoginManager()
uploaded_images = UploadSet('images', IMAGES)
principals = Principal()
rest_api = Api()


FACEBOOK_APP_ID = '297599923964208'
FACEBOOK_APP_SECRET = '1ef3edc1fcd6bf6ee465271ccce2bfc7'


#login manager stuff
login_manager.login_view = "main.login"
login_manager.session_protection = "strong"
login_manager.login_message = "Please login to access this page"
login_manager.login_message_category = "info"

@login_manager.user_loader
def load_user(userid):
    from models import User
    return User.query.get(userid)

#principal stuff for roles
admin_permission = Permission(RoleNeed('admin'))
poster_permission = Permission(RoleNeed('poster'))
default_permission = Permission(RoleNeed('default'))
