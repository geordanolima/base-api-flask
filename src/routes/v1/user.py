from flask_restx import Resource


class User(Resource):

    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)
        from src.models.user import UserModel, base_schemas

        self.model_class = UserModel
        self.model_schema = base_schemas

    def get(self):
        users = self.model_class.query.all()
        return self.model_schema.dump(users)
