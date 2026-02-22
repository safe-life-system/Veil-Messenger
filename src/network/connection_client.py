import ssl
import socket
import asyncio

#Класс подключения клиента
class ClientConnection:
    def __init__(self):
        self.reader = None
        self.writer = None
    
    #Реализация подключения к серверу
    async def connection_client(self,hostname, port, ssl_certificate):
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        context.load_verify_locations(ssl_certificate)
        context.check_hostname = False
        context.verify_mode = ssl.CERT_REQUIRED
        self.reader, self.writer = await asyncio.open_connection(
            host=hostname,
            port=port,
            ssl=context
        )
    
    #Реализация отправки сообщения 
    async def send_write(self, text):
        if not self.writer:
            print("Нет соединения")
            return
        self.writer.write(text)
        await self.writer.drain()
        print("Отправлено")
    
    #Реализация закрытия
    async def close(self):
        if self.writer:
            self.writer.close()
            await self.writer.wait_closed()