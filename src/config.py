class Config:
    SECRET_KEY = 'anythingwished'

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig()
}
