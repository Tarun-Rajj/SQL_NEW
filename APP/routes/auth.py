from flask import Blueprint,request,jsonify
from flask_login import login_user
from werkzeug.security import check_password_hash
from APP.models import User
from APP import db

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
#Extracting user details
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')

    # Validate the role
    valid_roles = ['admin', 'manager', 'employee']
    if role not in valid_roles:
        return jsonify({'message': 'Invalid role. Choose a valid role: admin, manager, employee.'}), 400

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'message': 'Username already exists. Choose a different username.'}), 400

    new_user = User(username=username, password=password, role=role)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User signed up successfully!'})


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    #Extracting login data i mean creadentials
    username = data.get('username')
    password = data.get('password')
    # role = data.get('role')

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        login_user(user)
        return jsonify({'message': 'Login successful!'})
    else:
        return jsonify({'message': 'Login unsuccessful. Please check your username and password.'}), 401



