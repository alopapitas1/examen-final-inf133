from database import db

class Restau(db.Model):
    __tablename__="reservas"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), nullable=False)
    address=db.Column(db.String(50), nullable=False)
    city=db.Column(db.String(50), nullable=False)
    phone=db.Column(db.String(50), nullable=False)
    desc=db.Column(db.String(50), nullable=False)
    rating=db.Column(db.Float(), nullable=False)
    
    
    def __init__(self,name,address,city,phone,desc,rating):
        self.name=name
        self.address=address
        self.city=city
        self.phone=phone
        self.desc=desc
        self.rating=rating
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self,name=None,address=None,city=None,phone=None,desc=None,rating=None):
        if name is not None:
            self.name=name
        if address is not None:
            self.address=address
        if city is not None:
            self.city=city
        if phone is not None:
            self.phone=phone
        if desc is not None:
            self.desc=desc
        if rating is not None:
            self.rating=rating
        db.session.commit()
        
    @staticmethod
    def get_all():
        return Restau.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Restau.query.get(id)
    
    