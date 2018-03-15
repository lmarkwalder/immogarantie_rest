import flask_restplus
import logging

api = flask_restplus.Api(version='1.0', title='Immogarantie API')
log = logging.getLogger(__name__)


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception ocurred'
    log.exception(message)
