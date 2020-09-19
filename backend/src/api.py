import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
# db_drop_and_create_all()

## ROUTES
@app.route("/drinks")
def getDrink():
    try:
        drinks = list(map(Drink.short, Drink.query.all()))
        return jsonify({
            "success": True,
            "drinks": drinks
        })
    except:
        abort(404) 

@app.route('/drinks-detail')
@requires_auth("get:drinks-detail")
def getDrinkDetails(payload):
    try:
        drinks = list(map(Drink.long, Drink.query.all()))
        return jsonify({
            "success": True,
            "drinks": drinks
        })
    except:
        abort(404)    

@app.route("/drinks", methods=['POST'])
@requires_auth("post:drinks")
def add_drinks(payload):
    body = request.get_json()
    print(body)
    drink_title = body.get('title', None)
    drink_recipe = body.get('recipe', None)
    if not drink_title or not drink_recipe:
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Title and recipe must be submitted.'
        }), 400
    drink = Drink(title=drink_title, recipe=json.dumps(drink_recipe))
    print(drink)
    try:
            drink.insert()
            return jsonify({
                'success': True,
                'drinks': [drink.long()]
            }), 200
    except Exception:
            abort(422)

@app.route('/drinks/<int:id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def patchDrinks(payload,id):
    body = request.get_json()
    drinktitle = body.get('title', None)
    drinkrecipe = body.get('recipe', None)
    if id is None:
        abort(400)
    drink = Drink.query.filter(Drink.id==id).one_or_none()
    if drink is None:
        abort(404)
    if drinktitle:
        drink.title = drinktitle
    if drinkrecipe:
        drink.recipe = json.dumps(drinkrecipe)
    try:
        drink.update()
        drink = Drink.query.filter(Drink.id==id).one_or_none()
        return jsonify({
            "success": True,
            "drinks": [drink.long()]
        })
    except Exception:
        abort(422)
        
@app.route('/drinks/<id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def deleteDrink(payload, id):
    drink = Drink.query.filter(Drink.id==id).one_or_none()
    if drink is None:
        abort(404)
    try:
        drink.delete()
        return jsonify({
            "success": True,
            "delete": id
        })
    except Exception:
        abort(422)

## Error Handling
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
         "success": False, 
         "error": 422,
        "message": "unprocessable"
     }), 422


@app.errorhandler(404)
def resource_not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "Unauthorized request"
    }), 401

@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "no data posted"
    }), 400

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "success": False,
        "error": 405,
        "message": "method not allowed"
    }), 405

@app.errorhandler(AuthError)
def auth_error(error):
    return jsonify({
        "success": False,
        "error": error.status_code,
        "message": error.error['description']
    }), error.status_code