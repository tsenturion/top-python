# client.py
import asyncio
import aiohttp
from aiohttp import WSMsgType, WSCloseCode
import logging
import signal
import sys
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

class WebSocketClient:
    def __init__(self, url):
        self.url = url
        self.session = None
        self.outgoing_queue = asyncio.Queue()
        self.retry_delay = 1.0
        self.max_retry_delay = 60.0
        self.connection_count = 0
        self.messages_received = 0
        self.messages_sent = 0
    
    async def connect_websocket(self):
        """Устанавливает WebSocket соединение с heartbeat"""
        if not self.session:
            self.session = aiohttp.ClientSession()
        
        return await self.session.ws_connect(
            self.url,
            heartbeat=30.0,
            timeout=10.0
        )
    
    async def handle_incoming(self, ws):
        """Обрабатывает входящие сообщения"""
        logger.info("✓ Начинаем слушать входящие сообщения")
        try:
            async for msg in ws:
                if msg.type == WSMsgType.TEXT:
                    self.messages_received += 1
                    logger.info(f"📩 Входящее #{self.messages_received}: {msg.data}")
                elif msg.type == WSMsgType.BINARY:
                    logger.info(f"📦 Бинарные данные: {len(msg.data)} байт")
                elif msg.type == WSMsgType.CLOSED:
                    logger.warning("⚠️  Соединение закрыто сервером")
                    break
                elif msg.type == WSMsgType.ERROR:
                    logger.error(f"❌ Ошибка WebSocket: {ws.exception()}")
                    break
        except Exception as e:
            logger.error(f"❌ Ошибка при чтении: {e}")
        finally:
            logger.info("✗ Обработка входящих сообщений завершена")
    
    async def handle_outgoing(self, ws):
        """Отправляет исходящие сообщения из очереди"""
        logger.info("✓ Начинаем отправку исходящих сообщений")
        try:
            while not ws.closed:
                try:
                    msg = await asyncio.wait_for(
                        self.outgoing_queue.get(),
                        timeout=1.0
                    )
                    if not ws.closed:
                        await ws.send_str(msg)
                        self.messages_sent += 1
                        logger.info(f"📤 Исходящее #{self.messages_sent}: {msg}")
                except asyncio.TimeoutError:
                    continue
        except Exception as e:
            logger.error(f"❌ Ошибка при отправке: {e}")
        finally:
            logger.info("✗ Отправка исходящих сообщений завершена")
    
    async def maintain_connection(self, shutdown_event):
        """Поддерживает WebSocket соединение с автоматическим переподключением"""
        try:
            while not shutdown_event.is_set():
                try:
                    self.connection_count += 1
                    logger.info(f"\n{'='*60}")
                    logger.info(f"🔌 Попытка подключения #{self.connection_count} к {self.url}")
                    logger.info(f"{'='*60}")
                    
                    ws = await self.connect_websocket()
                    logger.info("✅ WebSocket соединение установлено!")
                    logger.info(f"📊 Статистика: получено={self.messages_received}, отправлено={self.messages_sent}")
                    
                    # Сбрасываем задержку при успешном подключении
                    self.retry_delay = 1.0
                    
                    # Обрабатываем сообщения параллельно
                    async with asyncio.TaskGroup() as tg:
                        tg.create_task(self.handle_incoming(ws))
                        tg.create_task(self.handle_outgoing(ws))
                    
                    # Корректное закрытие
                    if not ws.closed:
                        logger.info("🔒 Закрываем соединение корректно")
                        await ws.close(code=WSCloseCode.GOING_AWAY)
                    
                except aiohttp.WSServerHandshakeError as e:
                    logger.error(f"❌ Ошибка handshake: {e}")
                except aiohttp.ClientError as e:
                    logger.error(f"❌ Ошибка клиента: {e}")
                except asyncio.TimeoutError:
                    logger.error("❌ Превышен timeout соединения")
                except ConnectionResetError:
                    logger.error("❌ Соединение сброшено")
                except Exception as e:
                    logger.error(f"❌ Неожиданная ошибка: {e}", exc_info=True)
                
                if shutdown_event.is_set():
                    break
                
                # Экспоненциальная задержка
                logger.info(f"⏳ Переподключение через {self.retry_delay:.1f} секунд...")
                try:
                    await asyncio.wait_for(
                        shutdown_event.wait(),
                        timeout=self.retry_delay
                    )
                    break
                except asyncio.TimeoutError:
                    pass
                
                self.retry_delay = min(self.retry_delay * 2, self.max_retry_delay)
        
        finally:
            if self.session:
                await self.session.close()
            logger.info("\n🛑 WebSocket клиент полностью остановлен")
            logger.info(f"📈 Итоговая статистика:")
            logger.info(f"   - Подключений: {self.connection_count}")
            logger.info(f"   - Получено сообщений: {self.messages_received}")
            logger.info(f"   - Отправлено сообщений: {self.messages_sent}")
    
    async def send_message(self, message):
        """Добавляет сообщение в очередь на отправку"""
        await self.outgoing_queue.put(message)

async def message_producer(client, shutdown_event):
    """Генерирует сообщения для отправки каждые 5 секунд"""
    counter = 0
    while not shutdown_event.is_set():
        await asyncio.sleep(5)
        if not shutdown_event.is_set():
            counter += 1
            message = f"Привет от клиента! Сообщение #{counter}"
            await client.send_message(message)

async def main():
    shutdown_event = asyncio.Event()
    
    # Кроссплатформенная обработка сигналов
    def signal_handler(signum, frame):
        logger.info("\n⚡ Получен сигнал остановки (Ctrl+C)")
        shutdown_event.set()
    
    # На Windows используем signal.signal, на Unix можно использовать add_signal_handler
    if sys.platform == 'win32':
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
    else:
        loop = asyncio.get_running_loop()
        for sig in (signal.SIGTERM, signal.SIGINT):
            loop.add_signal_handler(sig, lambda: signal_handler(sig, None))
    
    url = "ws://localhost:8088/ws"
    client = WebSocketClient(url)
    
    logger.info("🚀 Запуск WebSocket клиента")
    logger.info(f"🎯 Подключение к: {url}")
    logger.info("💡 Нажмите Ctrl+C для остановки\n")
    
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(client.maintain_connection(shutdown_event))
            tg.create_task(message_producer(client, shutdown_event))
    except* KeyboardInterrupt:
        logger.info("⚡ KeyboardInterrupt перехвачен")
        shutdown_event.set()
    except* Exception as eg:
        logger.info("Группа задач завершена с исключениями")
    
    logger.info("👋 Программа завершена")

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("⚡ Финальный перехват KeyboardInterrupt")