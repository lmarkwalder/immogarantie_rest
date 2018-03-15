import flask
import flask_restplus
from app.database.model.user import User as User_Model
import app.database.dao.user as user_dao
from app.api import immogarantie_api
from app.api.endpoints.schemas import user_schema

users_ns = immogarantie_api.namespace('users', description='User operations')


@users_ns.route('/')
class UserListAPI(flask_restplus.Resource):

    @immogarantie_api.marshal_with(user_schema, as_list=True)
    def get(self):
        """
        Returns list of users.
        """
        return User_Model.query.all()

    @immogarantie_api.response(201, 'User successfully created.')
    @immogarantie_api.expect(user_schema)
    def post(self):
        """
        Creates a new user.
        """
        data = flask.request.json
        user_dao.create_user(data)
        return None, 201


@users_ns.route('/<int:id>')
@immogarantie_api.response(404, 'User not found.')
class UserAPI(flask_restplus.Resource):

    @immogarantie_api.marshal_with(user_schema)
    def get(self, id):
        """
        Returns a user.
        """
        return User_Model.query.filter(User_Model.id == id).one()

    @immogarantie_api.expect(user_schema)
    @immogarantie_api.response(204, 'User successfully updated.')
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
        user_dao.update_user(id, data)
        return None, 204

    @immogarantie_api.response(204, 'User successfully deleted.')
    def delete(self, id):
        """
        Deletes a user.
        """
        user_dao.delete_user(id)
