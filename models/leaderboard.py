from pymongo.collection import Collection
from datetime import datetime

class LeaderboardModel:
    def __init__(self, db):
        self.collection: Collection = db["leaderboard"]

    def increment(self, pokemon_name):
        query = {"pokemon": pokemon_name.lower()}
        update = {"$inc": {"count": 1}, "$setOnInsert": {"first_seen": datetime.utcnow()}}
        self.collection.update_one(query, update, upsert=True)

    def get_top(self, n=5):
        cursor = self.collection.find().sort("count", -1).limit(n)
        return list(cursor)

    def reset(self):
        self.collection.delete_many({})
