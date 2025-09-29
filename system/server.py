# server.py
import asyncio
import aiohttp
from aiohttp import web
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WebSocketServer:
    def __init__(self):
        self.clients = set()
        self.message_counter = 0
    
    async def websocket_handler(self, request):
        """Обработчик WebSocket соединений"""
        ws = web.WebSocketResponse(heartbeat=30.0, timeout=10.0)
        await ws.prepare(request)
        
        client_id = id(ws)
        self.clients.add(ws)
        logger.info(f"Клиент {client_id} подключился. Всего клиентов: {len(self.clients)}")
        
        try:
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    logger.info(f"Получено от клиента {client_id}: {msg.data}")
                    # Отправляем подтверждение
                    await ws.send_str(f"Сервер получил: {msg.data}")
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    logger.error(f"Ошибка соединения с {client_id}: {ws.exception()}")
        finally:
            self.clients.discard(ws)
            logger.info(f"Клиент {client_id} отключился. Осталось клиентов: {len(self.clients)}")
        
        return ws
    
    async def broadcast_messages(self):
        """Периодически отправляет сообщения всем клиентам"""
        while True:
            await asyncio.sleep(3)
            if self.clients:
                self.message_counter += 1
                message = f"Broadcast #{self.message_counter}: Привет от сервера!"
                logger.info(f"Рассылка сообщения: {message}")
                
                # Отправляем всем подключенным клиентам
                for ws in list(self.clients):
                    try:
                        await ws.send_str(message)
                    except Exception as e:
                        logger.error(f"Ошибка отправки: {e}")
    
    async def simulate_disconnects(self):
        """Симулирует отключения для демонстрации переподключения"""
        await asyncio.sleep(15)  # Ждём 15 секунд
        logger.warning("СИМУЛЯЦИЯ: Принудительно закрываем все соединения!")
        
        for ws in list(self.clients):
            await ws.close(code=1001, message=b'Server restart simulation')
        
        logger.info("Все соединения закрыты. Ждём переподключения клиентов...")

async def main():
    server = WebSocketServer()
    app = web.Application()
    app.router.add_get('/ws', server.websocket_handler)
    
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8088)
    await site.start()
    
    logger.info("WebSocket сервер запущен на ws://localhost:8088/ws")
    
    # Запускаем фоновые задачи
    async with asyncio.TaskGroup() as tg:
        tg.create_task(server.broadcast_messages())
        tg.create_task(server.simulate_disconnects())

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Сервер остановлен")