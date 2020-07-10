from flask import Flask
from config import config_options

def create_app(config_name):
    # initialize app
    app = Flask(__name__, instance_relative_config=True)

    # app configurations
    app.config.from_object(config_options[config_name])

    # register blueprint
    from .main import main as main_bp
    app.register_blueprint(main_bp)

    return app