
from app.services.handler_json import read_json

def check_if_user_already_listed(filepath, email) -> bool:
    user_list = read_json(filepath)
    
    for user in user_list:
        if user['email'] == email:
            return True
        
def check_fields(filepath, user) -> bool:
    # field_list =  read_json(filepath)

    # for field in field_list:
    if type(user["nome"]) or type(user["email"]) != str:
        return True
    return False