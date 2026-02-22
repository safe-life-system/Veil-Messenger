import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine

from src.network import connection_client
import socket, asyncio
from qasync import QEventLoop, asyncSlot
from src.ux import backend
import os
import dotenv


def start():
    app = QApplication(sys.argv)

    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    engine = QQmlApplicationEngine()
    engine.load("ui/login.qml")

    client = connection_client.ClientConnection()
    
    async def setup():
        dotenv.load_dotenv("data\.env")
        host = os.getenv("IP_ADDRESS")
        port = os.getenv("PORT")
        certificate_path = os.getenv("CERTIFICATE_PATH")
        await client.connection_client(host, port,certificate_path)
        
    loop.create_task(setup())
    _backend = backend.Backend(client)
    engine.rootContext().setContextProperty("backend", _backend)

    with loop:
        loop.run_forever()