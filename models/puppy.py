from flask_sqlalchemy import SQLAlchemy
from config.alchemy_i import db 

class Puppy(db.Model):  
    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def __repr__(self):
        return f"Puppy {self.name} is {self.age} years old"

