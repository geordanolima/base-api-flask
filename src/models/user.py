from marshmallow import fields, EXCLUDE
from src import db, ma


class Base(db.Model):

    __abstract__  = True
    
    id = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(
        db.DateTime,
        default=db.func.current_timestamp()
    )
    date_modified = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp()
    )


class UserModel(Base):

    __tablename__ = "auth_user"
    __table_args__ = {'extend_existing': True}

    name = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=False)
    status = db.Column(db.Boolean, nullable=False)


class UserSchema(ma.Schema):

    class Meta:
        unknown = EXCLUDE
        fields = ('id', 'name', 'email', 'status')


base_schema = UserSchema()
base_schemas = UserSchema(many=True)
