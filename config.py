import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfg(Config):
    """
    configurations for prod environment inherits from Config
    """
    pass
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:123456@localhost/pitches_test'

class DevConfig(Config):
    """
    configurations for dev environment inherits from Config
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:123456@localhost/pitches'
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfg,
    'test': TestConfig
}