import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink, db
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




'''
@TODO implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''

# end point for get all drinks coffee from database and send as json file 
@app.route("/drinks") 
def get_drinks():
    # n=list(Drink.query.all())
    # drinks = list(map(Drink.short, Drink.query.all()))
    try:

        get_all_drink = Drink.query.all()
        # print(get_all_drink)
        if get_all_drink is None:
            abort(404)
        # convert all drinks from dadatbase to short form and save in drinks as list 
        # to send in result json
        drinks = [drink.short() for drink in get_all_drink]
        # print(drinks)
        return jsonify({
        'success': True,
        'drinks': drinks
        })

    except:
        abort(422)



# endpoint for get detials of all coffee but reuires auth befor can access
'''
@TODO implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''

@app.route('/drinks-detail')
#in autho make api with permission get detials of coffee
@requires_auth('get:drinks-detail')
def drink_details(token):
    try:

        get_drink = Drink.query.all()

        if get_drink is None:
            abort(404)

        drinks = [drink.long() for drink in get_drink]
        print(drinks)

        return jsonify({
            'success': True,
            'drinks': drinks
        }), 200

    except:
        abort(422)

    



'''
@TODO implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''


# endpoint for add new drinks
@app.route("/drinks", methods=['POST'])
@requires_auth('post:drinks')
def drink_post(token):
    try:
        if request.get_json():

            new_drink_data = request.get_json()
            print(new_drink_data)
            # print(new_drink_data)
            new_drink = Drink(title=new_drink_data['title'], recipe=json.dumps(new_drink_data['recipe'])).insert()
            print(json.dumps(new_drink_data['recipe']),new_drink_data['title'])
            # drinks = [drink.long() for drink in get_drink]
            drinks = list(map(Drink.long, Drink.query.all()))
            result = {
                "success": True,
                "drinks": drinks
            }
            return jsonify(result)
    except:
        abort (422)

    # get_new_recorde = request.get_json()
    # print(get_new_recorde)
    # return 'll'
    


'''
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''
#endpoint for change drinks
@app.route('/drinks/<drink_id>',methods=['PATCH'])
@requires_auth('patch:drinks')
def patch_drink(token,drink_id):
    try:

        if request.get_json():
            print(request.get_json)
            data = request.get_json()
            new_title = data['title']
            new_recipe = data['recipe']
            updatedrinks = Drink.query.get(drink_id)
            updatedrinks.title = new_title
            # convert javascript object to string to stor in database 
            updatedrinks.recipe = json.dumps(new_recipe)
            updatedrinks.update()
        #after update data we will return all drink data again
        drinks = [drink.long() for drink in Drink.query.all()]

        if drinks is None:
            abort(404)

        result = {
            "success":True,
            "drinks":drinks
        }

        return jsonify(result)

    except:
        abort(422)

'''
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''

@app.route('/drinks/<drink_id>',methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(token,drink_id):

    try:
        #select row from database which have id like drink_id
        drink_delete = db.session.query(Drink).filter(Drink.id == drink_id).one_or_none()
        if drink_delete is None:
            abort(404)
        #delete it 
        drink_delete.delete()



        result={
            "success":True,
            "delete":drink_id
        }

        return jsonify(result)

    except:
        abort(422)

''''''''''''







## Error Handling
'''
Example error handling for unprocessable entity
'''
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
                    "success": False, 
                    "error": 422,
                    "message": "unprocessable"
                    }), 422

'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False, 
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''

@app.errorhandler(404)
def resourceNotFound(error):
    return jsonify({
                    "success": False, 
                    "error": 404,
                    "message": "resource not found"
                    }), 404
'''
@TODO implement error handler for 404
    error handler should conform to general task above 
'''



'''
@TODO implement error handler for AuthError
    error handler should conform to general task above 
'''
@app.errorhandler(401)
def Unauthorized(error):
    return jsonify({
                    "success": False, 
                    "error": 401,
                    "message": "Unauthorized"
                    }), 401



@app.errorhandler(403)
def Forbidden(error):
    return jsonify({
                    "success": False, 
                    "error": 403,
                    "message": "Forbidden"
                    }), 403