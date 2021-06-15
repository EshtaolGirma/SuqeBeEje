from flask import Flask
from flask_restplus import Api
from sqlalchemy import create_engine

# Database Connection
engine = create_engine(
    'postgresql://esskerkggdswfg:c6f5f31c67e4ae3f5fa13e7c8576937d44a6b3d2a82202102e5621b4be8dfa75@ec2-54-197-100-79.compute-1.amazonaws.com:5432/d1085taktksfc4')



app = Flask(__name__)
api = Api(app, version='1.0', title='SuqeBeEje API',
          description='A SuqeBeEje shopping API')

from SuqeBeEja.controller import routes
