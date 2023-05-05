from src.provider import Provider

__all__ = [
    'main'
]

main = Provider()

db = main.db
ma = main.ma

from src.models.user import UserModel

main.migrate.init_app(main.app, db)
with main.app.app_context():
    db.create_all()
