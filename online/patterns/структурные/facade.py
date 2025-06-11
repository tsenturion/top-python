"""
facade

используем когда:
сложная система
разделяем клиентский код и внутренности
api проще
единый интерфейс к разным классам

клиент
подсистемы
фасад

adapter меняет интерфейс 
proxy контролирует доступ 
mediator управляет взаимодействием объектов

os
pandas numpy matplotlib
flask
subprocess.run()

(-)
скрывает важные возможности
если их нужно найти/увидеть больше гибкости, все-равно лезем внутрь
может превратить в бога-объект
"""

class DVDPlayer:
    def on(self):
        print('DVD вкл')

    def play(self):
        print("DVD play")

    def off(self):
        print("DVD выкл")

class Projector:
    def on(self):
        print('проектор вкл')

    def set_input(self, source):
        print(f"проектор источник {source}")

    def off(self):
        print("проектор выкл")

class AudioSystem:
    def on(self):
        print('аудиосистема вкл')

    def set_voulme(self, level):
        print(f"громкость установлена {level}")

    def off(self):
        print("аудиосистема выкл")

class HomeTheaterFacade:
    def __init__(self, dvd: DVDPlayer, projector: Projector, audio: AudioSystem):
        self.dvd = dvd
        self.projector = projector
        self.audio = audio

    def watch_movie(self):
        print("начало")
        self.projector.on()
        self.projector.set_input("DVD")
        self.audio.on()
        self.audio.set_voulme(100)
        self.dvd.on()
        self.dvd.play()
        print("готово")

    def end_movie(self):
        print("завершаем")
        self.dvd.off()
        self.audio.off()
        self.projector.off()

dvd = DVDPlayer()
projector = Projector()
audio = AudioSystem()

cinema = HomeTheaterFacade(dvd, projector, audio)

cinema.watch_movie()
cinema.end_movie()


"""
facade
онлайн-магазин

компоненты:
каталог товаров
система заказов
платежная система
уведомления

оформить заказ одним вызовом place_order()
"""

class Catalog:
    def get_product(self, product_id):
        print(f'[Catalog] получение информации о товаре {product_id}')
        return {'id': product_id, 'name': 'Ноутбук', 'price': 50000}

class OrderSystem:
    def create_order(self, user_id, product):
        print(f'[OrderSystem] создание заказа {product["name"]} для {user_id}')
        return {'order_id': 123, 'user_id': user_id, 'product': product}

class PaymentProcessor:
    def pay(self, user_id, amount):
        print(f'[PaymentProcessor] оплата заказа {user_id} за {amount}')
        return True

class NotificationService:
    def send_confirmation(self, user_id, message):
        print(f'[NotificationService] отправка уведомления {user_id} сообщение: {message}')

class ShopFacade:
    def __init__(self):
        self.catalog = Catalog()
        self.order_system = OrderSystem()
        self.payment = PaymentProcessor()
        self.notifier = NotificationService()

    def place_order(self, user_id: int, product_id: int):
        print(f'[ShopFacade] оформление заказа {user_id}')
        product = self.catalog.get_product(product_id)
        order = self.order_system.create_order(user_id, product)
        if self.payment.pay(user_id, product['price']):
            self.notifier.send_confirmation(user_id, f'ваш заказ №{order["order_id"]} оформлен')
        else:
            print('[ShopFacade] Ошибка оплаты')
        print('[ShopFacade] Заказ оформлен')




shop = ShopFacade()
shop.place_order(1, 1)


"""
система бронирования путешествий
подсистемы:
    бронирование авиабилетов
    бронирование отеля
    бронирование автобуса
    стравки

FlightBooking book_flight()
HotelBooking book_hotel()
TransferService book_transfer()
InsuranceService buy_insurance()

TravelFacade: book_all()
"""
class FlightBooking:
    def book_flight(self):
        print("Бронирование авиабилета")

class HotelBooking:
    def book_hotel(self):
        print("Бронирование отеля")

class TransferService:
    def book_transfer(self):
        print("Бронирование автобуса")

class InsuranceService:
    def buy_insurance(self):
        print("Покупка страховки")

class TravelFacade:
    def __init__(self):
        self.flight_booking = FlightBooking()
        self.hotel_booking = HotelBooking()
        self.transfer_service = TransferService()
        self.insurance_service = InsuranceService()

    def book_all(self):
        self.flight_booking.book_flight()
        self.hotel_booking.book_hotel()
        self.transfer_service.book_transfer()
        self.insurance_service.buy_insurance()
        
travel = TravelFacade()
travel.book_all()