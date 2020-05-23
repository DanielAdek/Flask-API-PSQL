import os
from settings import database_string as connection_url, secret, test_db_connection_url

class Config(object):
  """[summary]
    Parent configuration class.
  """
  DEBUG = False
  SECRET = secret()
  CSRF_ENABLED = True
  SQLALCHEMY_DATABASE_URI = connection_url()

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = test_db_connection_url()

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}