from flask import request, jsonify, redirect, url_for,Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Resource, Api
from extensions import db
from app.models.user import User
from flask_login import login_user, logout_user, login_required
from flask_restful import reqparse

class RegisterResource(Resource):
    def post(self):
        """
        Register a new user
        ---
        parameters:
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
                password:
                  type: string
        responses:
          201:
            description: User registered successfully
          400:
            description: Bad request
        """
        data = request.json
        password=data['password']
        hashed_password = generate_password_hash(password)
        new_user = User(first_name=data['first_name'],last_name=data['last_name'], email=data['email'], password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User registered successfully'}, 201

class LoginResource(Resource):
    def post(self):
        """
        Login a user
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
                password:
                  type: string
        responses:
          200:
            description: Login successful
          401:
            description: Invalid credentials
        """
        data = request.json
        email = data['email']
        password = data['password']

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return {'message': 'Login successful'}
        else:
            return {'message': 'Invalid credentials'}, 401

class LogoutResource(Resource):
    @login_required
    def get(self):
        """
        Logout a user
        ---
        responses:
          200:
            description: Logout successful
        """
        logout_user()
        return redirect(url_for('login'))

# Create API
authApi = Blueprint('authApi', __name__)
api = Api(authApi)

api.add_resource(RegisterResource, '/api/register')
api.add_resource(LoginResource, '/api/login')
api.add_resource(LogoutResource, '/api/logout')
