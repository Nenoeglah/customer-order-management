from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, validates
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from db import db

Base = declarative_base()

class Customer(db.Model):
    __tablename__ = 'customer'
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
    __tablename__ = 'order'
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

    @validates('amount')
    def validate_amount(self, key, amount):
        if amount <= 0:
            raise ValueError('Amount must be greater than zero')
        return amount

class User(db.Model):
    __tablename__ = 'user'
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

    @validates('password')
    def validate_password(self, key, password):
       
        if len(password) < 4:
            raise ValueError('Password must be at least 4 characters long')
        return password
