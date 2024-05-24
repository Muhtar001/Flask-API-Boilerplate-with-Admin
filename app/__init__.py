from flask import Flask
from extensions import db, login_manager
from config import Config
from .models.user import User
from flasgger import Swagger

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .models.user import User
    from .routes.auth import auth
    from .api.user import userApi
    from .api.auth import authApi
    from .routes.main import main
    from .admin.admin_views import admin, MyAdminIndexView, UserModelView

    app.register_blueprint(auth)
    app.register_blueprint(userApi)
    app.register_blueprint(authApi)
    app.register_blueprint(main)
    admin.init_app(app)

    swagger = Swagger(app)

    return app