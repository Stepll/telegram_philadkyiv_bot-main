"""
    
    


"""



""" Глобальні змінні """

administrator = 333592969 # Головний адміністратор
chat = -1001590303154  # Чат, куди надсилаються питання з боту. ПП замість чату використовувати для таких цілей не рекомендується.
admin_ids = [administrator, chat] # Список вповноважених адміністраторів 

BOT_TOKEN = "6254393413:AAGqZuU1thBXno-UKysR5uQtAfLK6mEL3Lw"    # Токен боту
MONGOSH_TOKEN = "mongodb://localhost:27017/"                    # Токен MongoDB
MONGOSH_DBASE = 'telegram_philadkyiv'                           # Назва бази данних


""" Конфігурація """

ANONQUEST = True    # True - питання надсилаються анонімними
                    # False - питання пересилаються від користувача з його іменем

WHITELIST = False   # True - права адміністратора мають лише ті, хто знаходиться в списку admin_ids
                    # False - права адміністратора мають усі учасники адмінського чату

SENDLOG = True      # True - при вимкнені боту головному адміністратору надсилаються файл з логами
                    # False - файл не надсилається
