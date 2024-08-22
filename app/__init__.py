from flask import Flask
from flask_login import LoginManager
from app.blueprints.home.routes import home
from app.blueprints.admin.routes import admin
from app.blueprints.auth.routes import auth
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username



def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.get_user_by_id(user_id)

    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(auth, url_prefix='/auth')

    return app
