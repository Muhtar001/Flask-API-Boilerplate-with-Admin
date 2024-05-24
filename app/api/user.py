from flask import request, jsonify,Blueprint
from flask_restful import Resource, Api
from extensions import db
from app.models.user import User
from flask_login import login_required
from flask_restful import reqparse
from app.utils.admin_check import admin_required


class UserResource(Resource):
    def get(self, user_id=None):
        """
        Get user(s)
        ---
        parameters:
          - in: path
            name: user_id
            type: integer
            required: false
            description: ID of the user to retrieve
        responses:
          200:
            description: User details
            schema:
              id: User
              properties:
                id:
                  type: integer
                first_name:
                  type: string
                last_name:
                  type: string
                email:
                  type: string
                avatar_path:
                  type: string
                about:
                  type: string
                isAdmin:
                  type: boolean
          404:
            description: User not found
        """
        if user_id:
            user = User.query.get(user_id)
            if user:
                return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email, 'avatar_path': user.avatar, 'about': user.about, 'isAdmin': user.isAdmin}
            else:
                return {'message': 'User not found'}, 404
        else:
            users = User.query.all()
            users_list = [{'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email, 'avatar_path': user.avatar, 'about': user.about, 'isAdmin': user.isAdmin} for user in users]
            return users_list

    @login_required
    @admin_required
    def post(self):
        """
        Create a new user
        ---
        parameters:
          - in: body
            name: body
            required: true
            schema:
              id: User
              properties:
                email:
                  type: string
                first_name:
                  type: string
                last_name:
                  type: string
        responses:
          201:
            description: User created successfully
          400:
            description: Bad request
        """
        data = request.json
        new_user = User(email=data['email'], first_name=data['first_name'], last_name=data['last_name'])
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User created successfully'}, 201
    @login_required
    @admin_required
    def put(self, user_id):
        """
        Update an existing user
        ---
        parameters:
          - in: path
            name: user_id
            type: integer
            required: true
            description: ID of the user to update
          - in: body
            name: body
            required: true
            schema:
              id: User
              properties:
                first_name:
                  type: string
                last_name:
                  type: string
                email:
                  type: string
                avatar:
                  type: string
        responses:
          200:
            description: User updated successfully
          404:
            description: User not found
        """
        user = User.query.get(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        data = request.json
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.email = data.get('email', user.email)
        user.avatar = data.get('avatar', user.avatar)
        db.session.commit()
        return {'message': 'User updated successfully'}

    @login_required
    def delete(self, user_id):
        """
        Delete a user
        ---
        parameters:
          - in: path
            name: user_id
            type: integer
            required: true
            description: ID of the user to delete
        responses:
          200:
            description: User deleted successfully
          404:
            description: User not found
        """
        user = User.query.get(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        db.session.delete(user)
        db.session.commit()
        return {'message': 'User deleted successfully'}


# Create API
userApi = Blueprint('userApi', __name__)
api = Api(userApi)

api.add_resource(UserResource, '/api/user', '/api/user/<int:user_id>')