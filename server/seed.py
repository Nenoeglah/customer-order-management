
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config
from models import Base, Customer, Order

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


customer1 = Customer(name='John Doe', code='JD001', phone_number='+254711966490')
customer2 = Customer(name='Jane Smith', code='JS002', phone_number='+254711123456')

order1 = Order(item='Laptop', amount=1500, customer_id=1, phone_number='+254711966490')
order2 = Order(item='Phone', amount=800, customer_id=2, phone_number='+254711123456')

session.add_all([customer1, customer2, order1, order2])
session.commit()

print("Data seeded successfully.")

