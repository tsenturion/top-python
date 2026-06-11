class User:
    def login(self):
        print("User logged in")
        
        
user = User()
user.login()


order.validate()
payment.process(order)
delivery.create(order)
notification.send(order)


class EmailService:
    def send(self, message):
        print("Отправка email")


class UserService:
    def register(self, user):
        email_service = EmailService()
        email_service.send("Пользователь зарегистрирован")
        sms.send()
        push.send()
        analytics.track()
        logger.write()
        

class Application:
    def login(self):
        pass
    
    def save_data(self):
        pass
    
    def send_email(self):
        pass
    
    def generate_report(self):
        pass
    
    def process_payment(self):
        pass
    

class PaymentProcessor:
    def process(self, payment_type):
        if payment_type == "card":
            print("Processing card payment")
        elif payment_type == "cash":
            print("Processing cash payment")
        else:
            print("Invalid payment type")
            
            
class A:
    def action(self):
        b.action()
        

user_registered()
"""
send_email()
create_profile()
write_log()
update_statistics()
send_notification()
"""

load_file()
validation_file()
parse_file()
save_data()

if validation_enabled:
    validate_data()
    
if compression_enabled:
    compress_data()
    
async def process():
    ...
    
    
class OrderProcessor:
    def process(self):
        ...
        
class ReportGenerator:
    def generate(self):
        ...