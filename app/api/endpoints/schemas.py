from flask_restplus import fields
from app.api import immogarantie_api

#validation schemas
user_schema = immogarantie_api.model('User', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a user'),
    'first_name': fields.String(required=True, description='last name'),
    'last_name': fields.String(required=True, description='first name'),
    'age': fields.Integer(required=True, description='Age'),
})
