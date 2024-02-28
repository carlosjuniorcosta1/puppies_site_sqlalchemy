import os 
from flask import Flask
from config.config import Config
from config.alchemy_i import db
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models.puppy import Puppy

class AppFactory:
    def __init__(self):
        self.basedir = os.path.abspath(os.path.dirname(__file__))
        self.app = Flask(__name__)
        self.app.config.from_object(Config)
        self.db = db
        self.db.init_app(self.app)

    def create_app(self):
        return self.app, self.db
    
    def create_table(self):
        with self.app.app_context():
            self.db.create_all()
    
app_factory = AppFactory()

app, db = app_factory.create_app()

Migrate(app, db)
