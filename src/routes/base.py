from src.routes.health import Healthcheck, HealthcheckError
from src.routes.v1.user import User


class Rotes():

    def __init__(self, api):
        self.api = api
        self.api.add_resource(User, '/v1/user')
        self.api.add_resource(Healthcheck, '/health')
        self.api.add_resource(HealthcheckError, '/health-error')

    def carrega_rotas(self):
        return self.api
