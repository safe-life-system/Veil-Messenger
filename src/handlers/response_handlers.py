import asyncio, json
from data.config import handlers_list
from src.db import data_base_control
import uuid

#Клас обработки ответов об сервера
class ResponseHandler:
    def __init__(self, response):
        self.response = json.loads(response)
        self.type_response = self.response["type_response"]
        
    #Метод распознавания типа ответа
    async def check_type(self):
        if self.type_response in handlers_list.handler_list:
            self.type_response = self.type_response.replace("(", "")
            self.type_response = self.type_response.replace(")", "")
            
            return await getattr(self, self.type_response)()
        return False
    
    #Метод регистрации в локлаьной БД
    async def REGISTRATION(self):
        if self.response["registration_status"] is True:
            registration_db = data_base_control.DataBaseControl(self.response["user_id"], self.response["user_name"], self.response["user_login"], self.response["password"], self.response["salt"])
            registration_db.create_db()
            registration_db.registration_db()
            return True
        return False
    
    def AUTHORIZATION(self):
        if self.response["authorization_status"] is True:
            registration_db = data_base_control.DataBaseControl(self.response["user_id"], self.response["user_name"], self.response["user_login"], self.response["password"], self.response["salt"])
            registration_db.create_db()
            registration_db.registration_db()
            return True
        return False