import logging
from os import environ, path


class Settings:

    def __init__(self) -> None:
        try:
            from dotenv import load_dotenv
            load_dotenv()
        except Exception as error:
            logging.error(error)

    @staticmethod
    def load_variables():
        return {
            "HOST": environ.get("HOST", "0.0.0.0"),
            "PORT": environ.get("PORT", 5000),
            "DEBUG": bool(environ.get("DEBUG", 1)),
            "SQLALCHEMY_DATABASE_URI": environ.get("SQLALCHEMY_DATABASE_URI", "sqlite:///./sql_app.db"),
            "ENVIRONMENT": environ.get("ENVIRONMENT", 'development'),
            "CSRF_SESSION_KEY": environ.get("CSRF_SESSION_KEY", "key"),
            "SECRET_KEY": environ.get("SECRET_KEY", "key"),
            "BASE_DIR": path.abspath(path.dirname(__file__))
        }


variables = Settings.load_variables()
for config in variables:
    globals()[config] = variables[config]
