import asyncio
import json
import hashlib
import base64
from Crypto.Hash import SHA3_512
from Crypto.Random import get_random_bytes
import secrets

#Класс регистрации
class RegistrationAuthorization:
    def __init__(self, user_login, user_name, password, user_id=None):
        self.user_login = user_login
        self.user_name = user_name
        self.password = password
        self.user_id = user_id
    
    #Реализация генерация соли
    def salt_geniration(self, user_login:str, user_password:str, salt:bytes=get_random_bytes(32)):
        user_login = bytes(user_login, "utf-8")
        user_password = bytes(user_password, encoding="utf-8")
        salt = salt[:len(salt)//2]+user_login+salt[len(salt)//2:]
        sault_user_password = salt[:len(salt)//2]+user_password+salt[len(salt)//2:]
        
        return {"salt": salt, "salt_user_password": sault_user_password}
    
    #Метод регистрации
    def registration(self):
        self.user_login = base64.b64encode(SHA3_512.new(bytes(self.user_login, "utf-8")).digest()).decode('utf-8')
        requesrt = {
            "type_request": "(REGISTRATION)",
            "user_login": self.user_login,
            "user_name": self.user_name,
            "password": self.password
        }
        
        return json.dumps(requesrt)
    
    def authorization(self):
        self.user_login = base64.b64encode(SHA3_512.new(bytes(self.user_login, "utf-8")).digest()).decode('utf-8')
        requesrt = {
            "type_request": "(AUTHORIZATION)",
            "user_login": self.user_login,
            "user_name": self.user_name,
            "password": self.password,
        }
        
        return json.dumps(requesrt)