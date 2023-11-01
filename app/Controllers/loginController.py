from flask import Blueprint, request, jsonify
from app import db
from ..Models import User
from ..DTO import StatusDTO
login_bp = Blueprint('auth',__name__)

#auth/login
@login_bp.route('/login' , methods = ["POST"])
def login():
    try:
        data = request.get_json()
        user_name=data['user_name']
        password=data['password']
        existing_user = User.query.filter_by(user_name=user_name).first()
        if not (existing_user):
            response =jsonify(StatusDTO(404,"User name not valid").__dict__)
            return response
        else:
            if password == existing_user.password:
                return jsonify(StatusDTO(200,"Login sucsses").__dict__)
            else:
                return jsonify(StatusDTO(404,"User Name or Password Invalid..!").__dict__)
    except Exception as e:
        return jsonify(StatusDTO(404,str(e)).__dict__)

#auth/users/
@login_bp.route('/users', methods=['PUT'])
def add_user():
    try:
        # Get data from the request body
        data = request.get_json()
        user_name=data['user_name']
        password=data['password']
        existing_user = User.query.filter_by(user_name=user_name).first()
        if existing_user:
            return jsonify()

        new_user = User(user_name=user_name,password=password)
        # Add the new user to the database session
        db.session.add(new_user)

        # Commit the changes to persist the new user in the database
        db.session.commit()

        # Return a success response
        return jsonify(StatusDTO(200,"User Registration Success").__dict__)
    except Exception as e:
        # Rollback in case of an error and return an error response
        db.session.rollback()
        return jsonify(StatusDTO(404,str(e)).__dict__), 500
    finally:
        # Close the database session
        db.session.close()
