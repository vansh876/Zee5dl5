from config import MONGO_DATABASE_NAME, MONGO_DATABASE_URL, BOT_USERNAME
import pymongo



class Database:
    def __init__(self, uri, database_name):
        self._client = pymongo.MongoClient(uri)
        self.db = self._client[database_name]
        self.misc = self.db['misc']

    def get_bot_stats(self):
        return self.misc.find_one({"bot": BOT_USERNAME})

    def create_config(self):
        self.misc.insert_one({
            'bot':BOT_USERNAME,
            'admins': [],
            'banned_users': [],
            'custom_caption':''
        })
    
    def update_stats(self, dict):
        myquery = {"bot": BOT_USERNAME}
        newvalues = {"$set" : dict}
        return self.misc.update_one(myquery, newvalues)


db = Database(MONGO_DATABASE_URL, MONGO_DATABASE_NAME)

