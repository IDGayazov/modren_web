from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)

pg_user = "postgres"
pg_pwd = "102455gi"
pg_port = "5433"

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://{username}:{password}@localhost:{port}/project".format(username=pg_user, password=pg_pwd, port=pg_port) 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = 'some-secret-string'

db = SQLAlchemy(app)

@app.before_request
def create_tables():
    db.create_all()

import service, orm


api.add_resource(service.AllUsers, "/users")
api.add_resource(service.UserRegustration, "/registration")