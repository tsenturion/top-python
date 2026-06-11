#плохо
if database_type == 'postgres':
    storage = PostgresStorage()
elif database_type == 'mysql':
    storage = MySQLStorage()
elif database_type == 'sqlite':
    storage = SQLiteStorage()
else:
    storage = APIStorage()
    
    
#лучше
def create_storage(database_type):
    if database_type == 'postgres':
        return PostgresStorage()
    elif database_type == 'mysql':
        return MySQLStorage()
    elif database_type == 'sqlite':
        return SQLiteStorage()
    else:
        return APIStorage()
    

storage = create_storage(config.database_type)


print('---------------------------------------------------')

class NotificationService:
    def __init__(self):
        self.sender = EmailSender()
        
    
class NotificationService:
    def __init(self, sender):
        self.sender = sender
        
sender = EmailSender()
service = NotificationService(sender)


repository = UserRepository(database)
logger = Logger()
cache = Cache()
service = UserService(repository, logger, cache)


user = get_user_service()


class Cat:
    pass

class Dog:
    pass

animal_class = Cat

animal = animal_class()

class PdfDocument:
    pass

class WordDocument:
    pass

class ExcelDocument:
    pass


def create_logger():
    if config.dubug:
        return DebugLogger()
    logger = Logger()
    logger.set_level(config.log_level)
    logger.enable_file_output()
    return ProductionLogger()