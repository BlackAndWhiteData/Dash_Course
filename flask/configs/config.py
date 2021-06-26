import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProductionConfig(Config):
    DEBUG = False


class DebugConfig(Config):
    DEBUG = True


config_dict = {
    'Debug': DebugConfig,
    'Production' : ProductionConfig
}