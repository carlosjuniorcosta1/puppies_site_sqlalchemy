import os 
from flask import Flask
from config.config import Config
from flask_sqlalchemy import SQLAlchemy

class AppFactory:
    def __init__(self):
        self.basedir = os.path.abspath(os.path.dirname(__file__))
        self.app = Flask(__name__)
        self.app.config.from_object(Config)
        self.db = SQLAlchemy(self.app)

    def create_app(self):
        return self.app, self.db
    
app_factory = AppFactory()

app, db = app_factory.create_app()








# def update_puppy(id, nome=None, idade=None):
#     with app.app_context():
#         up_puppy = Puppy.query.get(id)
#         if up_puppy:
#             if nome:
#                 up_puppy.name = nome
#             if idade:
#                 up_puppy.age = idade
#             db.session.commit()

