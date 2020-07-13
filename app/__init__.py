from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options

bootstrap = Bootstrap()
db = SQLAlchemy()
def create_app(config_name):
    # initialize app
    app = Flask(__name__, instance_relative_config=True)

    # app configurations
    app.config.from_object(config_options[config_name])
    bootstrap.init_app(app)
    db.init_app(app)

    # register blueprint
    from .main import main as main_bp
    app.register_blueprint(main_bp)

    return app