# Flask Project Builderplate

This is a useful boilerplate to kickstart your next Flask project. It includes several necessary features to help you get started quickly.

## Features Included
- **User Authentication**: User registration, login, and logout functionalities are provided.
- **User Management**: CRUD operations for managing users with roles like admin.
- **API Endpoints**: RESTful API endpoints for user-related operations.
- **Authorization**: Authorization mechanisms to restrict access to certain endpoints based on user roles.
- **Database Integration**: Integration with a database to store user information.
- **Flask Extensions**: Utilizes Flask extensions like Flask-RESTful, Flask-Login, and more.
- **Swagger Documentation**: API documentation using Swagger UI for easy testing and understanding.

## Getting Started
1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Configure your database settings in `config.py`.
4. Run the application using `python run.py`.
5. Access the application in your browser at `http://localhost:5000`.

### Creating New Model
To create a new model, follow these steps:
1. Define the model in the `models/your_model.py` file.
2. Create the necessary database migrations using Flask-Migrate.
3. Apply the migrations to update the database schema.

### Adding API URL
To add a new API URL, follow these steps:
1. Define the route in the `api/your_api.py` file.
2. Implement the necessary logic for the API endpoint.
3. Test the API endpoint using tools like Postman.

### Configure Admin from Model
To configure an admin user from the model, follow these steps:
1. Set the `isAdmin` field to `True` for the desired user in the database.
2. Ensure that the user has the necessary permissions to access admin features.
3. Test the admin functionality to verify access and permissions.


## Usage
- Register a new user using the `/api/register` endpoint.
- Login with the registered user using the `/api/login` endpoint.
- Access user management features like creating, updating, and deleting users.
- Explore the API documentation at `/apidocs` for detailed information on available endpoints.

## Contributing
Feel free to contribute to this project by submitting pull requests or raising issues.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.