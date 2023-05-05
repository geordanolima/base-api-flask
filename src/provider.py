from flask import Flask
from flask_restx import Api

from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from src.core.settings import Settings
from src.routes.base import Rotes


class Provider(Settings):

    def __init__(self):
        self.db = None
        self.migrate = None
        self.instance = None

        self.app = self.__create_app()
        self.config = self.load_variables()

        self.api = self.__create_api(self.app)
        Rotes(self.api).carrega_rotas()

    def __create_app(self):
        return Flask('api-base')

    def __create_api(self, app):
        instance = Api(
            app,
            title='API base',
            version="1.0.0",
            description='',
            doc="/docs",
            default='API',
            default_label='API Base'
        )
        instance.app.config.from_object('src.core.settings')
        instance.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        self.db = SQLAlchemy(instance.app)
        self.ma = Marshmallow(instance.app)
        self.migrate = Migrate(instance.app, self.db)

        return instance

    def run(self):
        self.api.app.run(
            host=self.config.get("host"),
            port=self.config.get("port"),
            debug=self.config.get("debug")
        )
