from flask import Flask,jsonify, request

from app.exc.already_in_list import AlreadyInListError
from app.exc.field_type_error import FieldTypeError
from http import HTTPStatus
from app.models.user import User


app = Flask(__name__)


@app.get('/user')
def get_users():
    return jsonify({"data": User.show_users()}), HTTPStatus.OK

@app.post('/user')
def add_user():
   
    user = User(**request.get_json())
    try:
        return {"data":user.save()} , HTTPStatus.CREATED
    except AlreadyInListError:
        return  {"error": "User already exists."}, HTTPStatus.CONFLICT
    