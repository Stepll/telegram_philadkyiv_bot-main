from datetime import datetime
from mongo.initialization import login


async def check_user(message):
        collection = await login('users')
        result = collection.find_one({"user_id": message.chat.id})
        if result == None:
                await full_registration(message, collection)
        else:
                print(result)
                # Тут має бути перевірка чи співпадають поточні данні до збережених та зміна данних в change
                

async def change(where_find, what_find, where_change, what_change):
        collection = await login('users')
        collection.replaceOne({where_find: what_find},{where_change: what_change})


async def full_registration(message, collection):
        post = {"first_name": message.chat.first_name,
                "last_name": message.chat.last_name,
                "username": message.chat.username,
                "user_id": message.chat.id,
                "blocked": False,
                "colonel": ["registration"],
                "created_at": datetime.now(),
                "edited_at": datetime.now()}

        collection.insert_one(post).inserted_id


async def get_user(user_id, collection):
        collection = await login('users')
        result = collection.find_one({"user_id": user_id})
        return result