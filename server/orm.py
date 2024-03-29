from main import db
from flask import jsonify
from sqlalchemy.schema import ForeignKey
from passlib.hash import pbkdf2_sha256 as sha256

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(120), nullable=True)
    lastname = db.Column(db.String(120), nullable=True)
    username = db.Column(db.String(120), unique=True, nullable=True)
    password = db.Column(db.String(120), nullable=True)
    role = db.Column(db.String(120), nullable=True)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(userrname=username).first()

    @classmethod
    def return_all(cls):
        def to_json(x):
            return{
                'username': x.username,
                'password': x.password
            }
        return {'users' : list(map(lambda x: to_json(x), UserModel.query.all()))}

    @staticmethod
    def generate_hash():
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)


