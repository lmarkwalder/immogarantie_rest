import flask_restplus
import logging

immogarantie_api = flask_restplus.Api(version='1.0', title='Immogarantie API')
log = logging.getLogger(__name__)


@immogarantie_api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception ocurred'
    log.exception(message)
