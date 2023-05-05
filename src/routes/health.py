from flask_restx import Resource
from src.utils.errors import Errors


class Healthcheck(Resource):

    def get(self):
        """
        Metodo para validar se a API está disponível util para algum serviço de monitoria.

        Returns:
            Caso a api esteja funcionando, retorna ok
        """
        return {'Status': 'ok'}


class HealthcheckError(Resource):

    def get(self):
        """ Metodo para validar se a API está retornando erros corretamente util para algum serviço de monitoria.

        Returns:
            Caso a api esteja funcionando, retorna mensagem de erro
        """
        try:
            print('erro_forcado: {}'.format(1 / 0))
        except Exception as erro:
            raise Errors().retorn_error(
                mensage='Retorno invalido.',
                error=erro
            )
