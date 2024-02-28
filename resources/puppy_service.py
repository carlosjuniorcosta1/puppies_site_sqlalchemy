from models.puppy import Puppy
from config.alchemy_i import db 
from basic import app

class PuppyService:
    def __init__(self):
        pass
    
    def read_puppies(self):  
        with app.app_context():
            all_puppies = Puppy.query.all()
            print(all_puppies)
            return all_puppies
        
    def read_puppy(self, id):
        with app.app_context():
            puppy = Puppy.query.get(1)
            print(puppy)
            return puppy

    def create_puppy(self, nome_cachorro, idade):
        with app.app_context():
            my_puppy = Puppy(nome_cachorro, idade)
            db.session.add(my_puppy)
            db.session.commit()

    def update_puppy(self, id, nome=None, idade=None):
        with app.app_context():
            up_puppy = Puppy.query.get(id)
            if up_puppy:
                if nome:
                    up_puppy.name = nome 
                if idade:
                    up_puppy.age = idade
                db.session.commit()
                    



    

    
