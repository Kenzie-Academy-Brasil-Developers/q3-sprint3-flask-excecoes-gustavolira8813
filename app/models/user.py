
from flask import jsonify
from app.exc.field_type_error import FieldTypeError
from app.services.handler_json import read_json, write_json
from app.services.user_services import check_if_user_already_listed, check_fields
from app.exc.already_in_list import AlreadyInListError
class User:
    FILENAME = "./app/database/database.json"
    def __init__(self, nome, email) -> None:
        self.nome = nome.capitalize()
        self.email = email.lower()
    
    @classmethod
    def show_users(cls) -> list[dict]:
        return read_json(cls.FILENAME)
    
    def save(self):
        user = self.__dict__
        if check_if_user_already_listed(self.FILENAME, user["email"]):
            raise AlreadyInListError
        return write_json(self.FILENAME, user)