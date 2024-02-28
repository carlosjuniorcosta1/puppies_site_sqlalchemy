from flask_sqlalchemy import SQLAlchemy

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:jose1984br@localhost:3306/banconovo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
