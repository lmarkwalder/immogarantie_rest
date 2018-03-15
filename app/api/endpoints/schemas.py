from flask_restplus import fields
from .. import api

user_schema = api.model('User', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a user'),
    'first_name': fields.String(required=True, description='last name'),
    'last_name': fields.String(required=True, description='first name'),
    'age': fields.Integer(required=True, description='Age'),
})
