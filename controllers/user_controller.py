from flask import Response, request, jsonify
from models.User import db, User
# from flask_sqlalchemy import SQLAlchemy

import json

# db = SQLAlchemy()

def index():
  session = db.session()
  users = session.query(User).all()
  users_json = [user.serialize() for user in users]
  session.close()

  return Response(json.dumps(users_json))

def show():
  return 

def create():
  body = request.get_json()
  session = db.session()

  existing_user = User.query.filter_by(name=body['name']).first()
  if existing_user:
    return jsonify({'error': 'This name is already in use.'}), 400

  try:
    user = User(name=body['name'], age=body['age'], address=body['address'])
    session.add(user)
    session.commit()
    return Response(json.dumps([user.serialize()]))
  except Exception as e:
    session.rollback()
  finally:
    session.close()

def edit():
  return 

def destroy():
  return 