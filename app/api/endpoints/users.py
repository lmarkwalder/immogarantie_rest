import flask
import flask_restplus
from app.database.model.user import User as User_Model
from app.database.dao.user import create_user, delete_user, update_user
from app.api import api
from app.api.endpoints.schemas import user_schema

users_ns = api.namespace('users', description='User operations')


@users_ns.route('/')
class UserListAPI(flask_restplus.Resource):

    @api.marshal_with(user_schema, as_list=True)
    def get(self):
        """
        Returns list of users.
        """
        return User_Model.query.all()

    @api.response(201, 'User successfully created.')
    @api.expect(user_schema)
    def post(self):
        """
        Creates a new user.
        """
        data = flask.request.json
        create_user(data)
        return None, 201


@users_ns.route('/<int:id>')
@api.response(404, 'User not found.')
class UserAPI(flask_restplus.Resource):

    @api.marshal_with(user_schema)
    def get(self, id):
        """
        Returns a .
        """
        return User_Model.query.filter(User.id == id).one()

    @api.expect(user_schema)
    @api.response(204, 'User successfully updated.')
    def put(self, id):
        """
        Updates a user.
        Use this method to update a user
        * Send a JSON object with the new name in the request body.
        ```
        {
          "first_name": "Vladimir",
          "last_name": "Trump"
        }
        ```
        * Specify the ID of the category to modify in the request URL path.
        """
        data = flask.request.json
        update_user(id, data)
        return None, 204

    @api.response(204, 'User successfully deleted.')
    def delete(self, id):
        """
        Deletes a user.
        """
        delete_user(id)
