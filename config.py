import os

class Config:
    NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/sources?language=en&apiKey=267d7fe5843144d9b8f75ea889ea51f7'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=267d7fe5843144d9b8f75ea889ea51f7'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}


