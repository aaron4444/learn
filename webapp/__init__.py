
from flask import Flask, render_template, url_for, redirect, session
#from models import db
from .controllers.main import main_blueprint

from .config import DevConfig


def create_app(object_name):

    app = Flask(__name__)
    app.config.from_object(object_name)

    #db.init_app(app)


    #go from gen initialization to the specific bluepint
    @app.route('/')
    def index():
        return redirect(url_for('main.home'))

    app.register_blueprint(main_blueprint)

    return app

if __name__ == '__main__':
    app.run()
