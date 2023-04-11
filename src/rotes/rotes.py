from .health import Healthcheck, HealthcheckError


class Rotes():
    def __init__(self, api):
        self.api = api
        self.api.add_resource(Healthcheck, '/health')
        self.api.add_resource(HealthcheckError, '/health-error')

    def carrega_rotas(self):
        return self.api
