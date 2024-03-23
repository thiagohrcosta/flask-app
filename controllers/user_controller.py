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

def show(user_id):
  session = db.session()
  try:
    user = session.query(User).get(user_id)
    return Response(json.dumps([user.serialize()]))
  except Exception as e:
    session.rollback()
    return {'message': 'User not found!'}
  finally:
    session.close()
 
def create():
  body = request.get_json()
  session = db.session()

  existing_user = User.query.filter_by(name=body['name']).first()
  if existing_user:
    return jsonify({'message': 'This name is already in use.'}), 400

  try:
    user = User(name=body['name'], age=body['age'], address=body['address'])
    session.add(user)
    session.commit()
    return Response(json.dumps([user.serialize()]))
  except Exception as e:
    session.rollback()
  finally:
    session.close()

def update(user_id):
  session = db.session()
  user = session.query(User).get(user_id)
  
  if not user:
    return jsonify({'message': 'User not found!'}), 404
  
  body = request.get_json()
  existing_user = User.query.filter_by(name=body['name']).first()
 
  if existing_user:
    return jsonify({'message': 'This name is already in use.'}), 400
  else:
    try:
      if body and body['name']:
        user.name = body['name']
      if body and body['age']:
        user.age = body['age']
      
      if body and body['address']:
        user.address = body['address']

      session.commit()
      return Response(json.dumps([user.serialize()]))

    except Exception as e:
      session.rollback()
      return jsonify({'message': 'An error occurred while attempting to update the user.'})
    finally:
      session.close()

def destroy(user_id):
  session = db.session()
  user = session.query(User).get(user_id)

  if not user:
    return jsonify({'message': 'User not found!'}), 404
  
  try:
    session.delete(user)
    session.commit()
    return jsonify({'message': 'User successfully deleted.'})
  except Exception as e:
    session.rollback()
    return jsonify({'message': 'An error ocurred while attempting to delete the user.'})
  finally:
    session.close()
  