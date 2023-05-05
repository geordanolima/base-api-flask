from src.rotes.health import Healthcheck, HealthcheckError
from src.rotes.user import User


class Rotes():
    def __init__(self, api):
        self.api = api
        self.api.add_resource(User, '/user')
        self.api.add_resource(Healthcheck, '/health')
        self.api.add_resource(HealthcheckError, '/health-error')

    def carrega_rotas(self):
        return self.api
