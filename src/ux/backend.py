from qasync import asyncSlot
from PySide6.QtCore import QObject
import struct
from src.services import registration

#Класс бэкэнда для QML
class Backend(QObject):
    def __init__(self, client, engine):
        super().__init__()
        self.client = client
        self.engine = engine

    @asyncSlot(str, str, str)
    async def registration(self, user_login, user_name, password):
        
        registration_data = registration.RegistrationAuthorization(user_login, user_name, password).registration().encode('utf-8')
        
        await self.client.send_write(struct.pack('!I', len(registration_data)))
        await self.client.send_write(registration_data)
        db_status = await self.client.handler_reader()
        if db_status is True:
            root = self.engine.rootObjects()[0]
            root.showMain()
            
    @asyncSlot(str, str, str)
    async def authorization(self, user_login, user_name, password):
        registration_data = registration.RegistrationAuthorization(user_login, user_name, password).authorization().encode('utf-8')
        
        await self.client.send_write(struct.pack('!I', len(registration_data)))
        await self.client.send_write(registration_data)
        db_status = await self.client.handler_reader()
        if db_status is True:
            root = self.engine.rootObjects()[0]
            root.showMain()