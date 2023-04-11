from flask import Flask
from flask_restx import Api
from src.rotas.rotes import Rotes


class Provider():
    def __init__(self):
        self.app = self.__create_app()
        api = self.__create_api(self.app)
        Rotes(api).carrega_rotas()

    def __create_app(self):
        return Flask('api-base')

    def __create_api(self, app):
        return Api(
            app,
            version='1.0.0',
            title='API base',
            description='',
            doc="/docs",
            default='api',
            default_label='api base'
        )

    # def _seeder(self, recriar=False):
        # from src.seeder.arq import seeder
        # seed = seeder()
        # seed.create(recriar)

    def run(self, app):
        # self._seeder()
        app.run()
