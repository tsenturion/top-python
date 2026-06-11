class Database:
    def save(self, data):
        print(f"Saving data: {data}")
        
#плохо        
class UserService:
    def __init__(self):
        self.database = Database()
        
    def create_user(self, user_data):
        self.database.save(user_data)
        
        
        
class LegacyPrinter:
    def print(self, document):
        print(f"Printing document: {document}")
        
        
class ReportGenerator:
    def generate_report(self, priter):
        priter.print("Report content")
        
        
        
class Product:
    pass

class Order:
    pass

class Payment:
    pass

class Delivery:
    pass

class Notification:
    pass

payment.process(order)

delivery.create(order)

notification.send(order)


class UserService:
    def __init__(self):
        #self.database = Database()
        self.database = database
        
        
class Logger:
    def log(self, message):
        print(message)
        
class Service:
    def __init__(self, database, logger):
        self.database = database
        self.logger = logger
        
image.load()
image.resize()
image.compress()
image.optimize()
image.save()


class File:
    pass

class Directory:
    pass

item.show()


class PaymentService:
    def __init__(self):
        self.client = ExternalPaymentClient()
        
    def pay(self, amount):
        self.client.make_payment(amount)