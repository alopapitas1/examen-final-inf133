from database import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
import json

class User(db.Model,UserMixin):
    __tablename__="user"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50),nullable=False,unique=True)
    email=db.Column(db.String(50),nullable=False)
    password=db.Column(db.String(50),nullable=False)
    phone=db.Column(db.String(50),nullable=False)
    roles=db.Column(db.String(50),nullable=False)
    
    def __init__(self,name,email,password,phone,roles=["user"]):
        self.name=name
        self.email=email
        self.password=generate_password_hash(password)
        self.phone=phone
        self.roles=json.dumps(roles)
        
    def save(self):
        db.session.add(self)
        db.session.commit()