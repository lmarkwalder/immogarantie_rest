import os
import flask
from flask_migrate import Migrate
import app.config as Config
from app.api import api
from app.api.endpoints import users_ns
from app.database.setup import db


def create_app(config=None, app_name=None, blueprints=None):
    '''Create a Flask app.'''

    if app_name is None:
        app_name = Config.DefaultConfig.PROJECT

    app = flask.Flask(app_name)
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    blueprint = flask.Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(users_ns)
    app.register_blueprint(blueprint)
    migrate = Migrate(app, db)
    db.init_app(app)
    return app


def configure_app(app, config=None):
    '''Handle different configurations'''
    app.config.from_object(Config.DefaultConfig)

    if config:
        app.config.from_object(config)

    application_mode = os.getenv('APPLICATION', 'LOCAL')
    app.config.from_object(Config.get_config(application_mode))


def configure_blueprints(app, blueprints):
    for blueprints in blueprints:
        app.register_blueprint(blueprint)


def configure_extensions(app):
    pass


def configure_logging(app):
    pass


def configure_error_handlers(app):
    @app.errorhandler(500)
    def server_error_page(error):
        return "ERROR PAGE"
