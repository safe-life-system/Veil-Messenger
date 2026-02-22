from qasync import asyncSlot
from PySide6.QtCore import QObject

#Класс бэкэнда для QML
class Backend(QObject):
    def __init__(self, client):
        super().__init__()
        self.client = client

    @asyncSlot()
    async def greet(self):
        await self.client.send_write(b"TEST")