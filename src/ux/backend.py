from qasync import asyncSlot
from PySide6.QtCore import QObject
import struct
from src.services import registration

#Класс бэкэнда для QML
class Backend(QObject):
    def __init__(self, client):
        super().__init__()
        self.client = client

    @asyncSlot(str, str, str)
    async def registration(self, user_login, user_name, password):
        
        registration_data = registration.RegistrationAuthorization(user_login, user_name, password).registration().encode('utf-8')
        
        await self.client.send_write(struct.pack('!I', len(registration_data)))
        await self.client.send_write(registration_data)
        await self.client.handler_reader()