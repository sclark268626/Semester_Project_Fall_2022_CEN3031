from cryptography.fernet import Fernet
import data
from enum import Enum


class NewUserOptions(Enum):
    USER_CREATED = 0
    USER_EXISTS = 1
    PAS_MISMATCH = 2


def login(user_id, pas):
    try:
        key = data.users[user_id].key
        decrypted_pass = key.decrypt(data.users[user_id].get_user_pas()).decode()
        if (data.users[user_id].get_user_pas() is not None) & (decrypted_pass == pas):
            return True
        else:
            return False
    except:
        return False


def new_user(user_id, pas, pas_conf):
    if data.users.get(user_id):
        return NewUserOptions.USER_EXISTS

    if pas != pas_conf:
        return NewUserOptions.PAS_MISMATCH

    key = Fernet(Fernet.generate_key())
    data.new_user(user_id, key.encrypt(pas.encode()), key)
    return NewUserOptions.USER_CREATED