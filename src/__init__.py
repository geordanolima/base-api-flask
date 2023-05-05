from src.provider import Provider
main = Provider()

db = main.db
ma = main.ma

from src.models.user import UserModel

main.migrate.init_app(main.app, db)
with main.app.app_context():
    db.create_all()
