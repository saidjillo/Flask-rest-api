from werkzeug.security import safe_str_cmp

from project.accounts.models import UserModel

    
def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user:
        return user


def identity(payload): 
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)