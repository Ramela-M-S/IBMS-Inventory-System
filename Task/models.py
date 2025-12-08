from Task import db
from flask_login import UserMixin


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),nullable = False)
    price = db.Column(db.Integer,nullable = False)
    stock = db.Column(db.Integer, nullable= False)
    image_file = db.Column(db.String(100),nullable=True, default= "default.jpg")
    
    def __repr__(self):
        return f"Item('{self.name}',{self.price})"

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),nullable= False, unique = True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(60))
    
     
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Purchase(db.Model):
    id = db.Column(db.Integer,primary_key= True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"))
    quantity = db.Column(db.Integer, nullable = False)
    Tot_price = db.Column(db.Integer, nullable = False)
    
    user = db.relationship("User", backref="purchases", lazy = True)
    item = db.relationship("Item", backref="purchases", lazy = True)
    
    def __repr__(self):
        return f"Purchase('{self.user_id}', '{self.item_id}')"
    
class Feedback(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    message = db.Column(db.String, nullable = False)
    
    def __repr__(self):
        return f"Feedback('{self.user_id}', '{self.message}')"