from aiogram.filters.base import Filter
from mongo.initialization import login


class Blocked(Filter):
    def __init__(self, blocked):
        self.blocked = blocked

    async def __call__(self, msg):
        collection = await login('users')
        result = collection.find_one({"user_id": msg.chat.id},{"_id": 0, "blocked": 1})
        if result == None:
            return True

        return result['blocked'] == self.blocked