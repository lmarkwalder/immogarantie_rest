import os
import flask
import flask_migrate
import app.config as Config
import app.api as Api
import app.database as Database


def create_app(config=None, app_name=None, blueprints=None):
    '''Create a Flask app.'''

    if app_name is None:
        app_name = Config.DefaultConfig.PROJECT

    #create flask app
    app = flask.Flask(app_name)

    configure_extensions(app)

    #set main route after localhost:5000
    blueprint = flask.Blueprint('api', __name__, url_prefix='/api')
    Api.immogarantie_api.init_app(blueprint)
    #add the namespaces for the api => localhost:5000/api/<namespace>
    Api.immogarantie_api.add_namespace(Api.endpoints.users_ns)
    app.register_blueprint(blueprint)

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
    #configure sqlite db
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database', 'sqlite_db.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    Database.db.init_app(app)
    #configure flask migrate
    migrate = flask_migrate.Migrate(app, Database.db)

def configure_logging(app):
    pass


def configure_error_handlers(app):
    @app.errorhandler(500)
    def server_error_page(error):
        return "ERROR PAGE"
