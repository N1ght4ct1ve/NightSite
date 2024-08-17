from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Konfiguration laden
    app.config.from_object('config.Config')
    
    # Blueprints registrieren
    from .blueprints.home import home as home_blueprint
    app.register_blueprint(home_blueprint)
    
    from .blueprints.admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    
    return app
