import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUG = False
    REPO_TYPE = os.getenv('REPO_TYPE', 'in_memory')

class DevelopmentConfig(Config):
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUG = False
    REPO_TYPE = os.getenv('REPO_TYPE', 'in_memory')

class TestingConfig(Config):
    TESTING = True
    REPO_TYPE = os.getenv('REPO_TYPE', 'in_memory')

class ProductionConfig(Config):
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUG = False
    REPO_TYPE = os.getenv('REPO_TYPE', 'in_file')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}