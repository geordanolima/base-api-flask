from werkzeug.exceptions import BadRequest


class Errors():

    def retorn_error(self, mensage, error):
        bad_request = BadRequest()
        bad_request.data = {
            'Error': mensage,
            'Detail': str(error)
        }
        return bad_request
