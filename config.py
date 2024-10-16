import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUB = False

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development' : DevelopmentConfig,
    'default' : DevelopmentConfig
}