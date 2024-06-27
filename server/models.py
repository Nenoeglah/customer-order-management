

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, validates
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from app import db

Base = declarative_base()

class Customer(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    code = Column(String(10), nullable=False, unique=True)
    phone_number = Column(String(15), nullable=False, unique=True)
    orders = relationship('Order', backref='customer', lazy=True)
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'phone_number': self.phone_number
        }

class Order(db.Model):
    id = Column(Integer, primary_key=True)
    item = Column(String(100), nullable=False)
    amount = Column(Integer, nullable=False)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    phone_number = Column(String(15), nullable=False)
    date_created = Column(DateTime, default=datetime.utcnow)
    
    def serialize(self):
        return {
            'id': self.id,
            'item': self.item,
            'amount': self.amount,
            'customer_id': self.customer_id,
            'phone_number': self.phone_number,
            'date_created': self.date_created
        }

class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(200), nullable=False)
    
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
