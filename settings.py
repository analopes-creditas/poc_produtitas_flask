import os


class BaseConfig:
    """ Base configuration. """

    SECRET_KEY = os.getenv('SECRET_KEY', '')
    FLASK_DEBUG = False
    CORS_ENABLED = False
    TESTING = False
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://127.0.0.1:6379')
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://127.0.0.1:6379')


class DevelopmentConfig(BaseConfig):
    """ Deployment configuration. """
    
    FLASK_ENV = 'deployment'
    FLASK_DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    """ Production configuration. """

    FLASK_ENV = 'production'
    CORS_ENABLED = True
