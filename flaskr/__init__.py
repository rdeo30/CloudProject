import os
from flask import Flask
from . import db
from . import auth

#contain the application factory, and it tells Python that the flaskr directory should be treated as a package.

def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True) 
    #relative filenames for loading the config are assumed
    #to be relative to the instance path instead of the application root.

    app.config.from_mapping(SECRET_KEY='dev', DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    os.makedirs(app.instance_path, exist_ok=True)

    @app.route('/hello')
    def hello():
        return "Hello World!"

    db.init_app(app)
    app.register_blueprint(auth.bp) #auth blueprint will have views to register new users and to log in and log out.

    return app