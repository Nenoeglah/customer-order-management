

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_oidc import OpenIDConnect
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
from models import Customer, Order, User
import africastalking

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
oidc = OpenIDConnect(app)

africastalking.initialize(Config.AFRICASTALKING_USERNAME, Config.AFRICASTALKING_API_KEY)
sms = africastalking.SMS

@app.before_first_request
def create_tables():
    db.create_all()

def send_sms(recipient, message):
    try:
        response = sms.send(message, [recipient])
        return response
    except Exception as e:
        print('Error sending SMS:', str(e))
        return None

@app.route('/auth', methods=['POST'])
def auth():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirm_password')
    
    if not username or not email or not password or not confirm_password:
        return jsonify({'message': 'All fields are required'}), 400
    
    if password != confirm_password:
        return jsonify({'message': 'Passwords do not match'}), 400
    
    if data.get('action') == 'login':
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({'message': 'Invalid credentials'}), 401
        return jsonify({'message': 'Login successful'}), 200
    
    if data.get('action') == 'create_account':
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({'message': 'Username already exists'}), 400
        
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'Account created successfully'}), 201
    
    return jsonify({'message': 'Invalid action'}), 400

@app.route('/customers', methods=['POST'])
@oidc.require_login
def add_customer():
    data = request.json
    new_customer = Customer(name=data['name'], code=data['code'], phone_number=data['phone_number'])
    db.session.add(new_customer)
    db.session.commit()
    return jsonify(new_customer.serialize()), 201

@app.route('/customers/<int:id>', methods=['PUT'])
@oidc.require_login
def update_customer(id):
    data = request.json
    customer = Customer.query.get_or_404(id)
    customer.name = data.get('name', customer.name)
    customer.code = data.get('code', customer.code)
    customer.phone_number = data.get('phone_number', customer.phone_number)
    db.session.commit()
    return jsonify(customer.serialize()), 200

@app.route('/customers/<int:id>', methods=['DELETE'])
@oidc.require_login
def delete_customer(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    return jsonify({'message': 'Customer deleted successfully'}), 200

@app.route('/customers', methods=['GET'])
@oidc.require_login
def get_customers():
    customers = Customer.query.all()
    return jsonify([customer.serialize() for customer in customers]), 200

@app.route('/orders', methods=['POST'])
@oidc.require_login
def add_order():
    data = request.json
    new_order = Order(
        item=data['item'],
        amount=data['amount'],
        customer_id=data['customer_id'],
        phone_number=data['phone_number']
    )
    db.session.add(new_order)
    db.session.commit()

    customer = Customer.query.get(data['customer_id'])
    if customer:
        message = f"Dear {customer.name}, your order for {new_order.item} has been placed successfully."
        send_sms(new_order.phone_number, message)

    return jsonify(new_order.serialize()), 201

@app.route('/orders/<int:id>', methods=['PUT'])
@oidc.require_login
def update_order(id):
    data = request.json
    order = Order.query.get_or_404(id)
    order.item = data.get('item', order.item)
    order.amount = data.get('amount', order.amount)
    order.customer_id = data.get('customer_id', order.customer_id)
    order.phone_number = data.get('phone_number', order.phone_number)
    db.session.commit()
    return jsonify(order.serialize()), 200

@app.route('/orders/<int:id>', methods=['DELETE'])
@oidc.require_login
def delete_order(id):
    order = Order.query.get_or_404(id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order deleted successfully'}), 200

@app.route('/orders', methods=['GET'])
@oidc.require_login
def get_orders():
    orders = Order.query.all()
    return jsonify([order.serialize() for order in orders]), 200

if __name__ == '__main__':
    app.run(debug=True)
