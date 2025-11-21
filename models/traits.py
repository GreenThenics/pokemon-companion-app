from pymongo.collection import Collection
from bson.son import SON
import random

class TraitsModel:
    def __init__(self, db):
        self.collection: Collection = db["traits_mapping"]

    def get_pokemon_for_traits(self, traits):
        pipeline = [
            {"$match": {"trait": {"$in": traits}}},
            {"$project": {"pokemon": 1}},
            {"$unwind": "$pokemon"},
            {"$group": {"_id": "$pokemon", "matches": {"$sum": 1}}},
            {"$sort": SON([("matches", -1), ("_id", 1)])}
        ]
        results = list(self.collection.aggregate(pipeline))
        if not results:
            return None
        weighted = []
        for r in results:
            weighted.extend([r["_id"]] * r["matches"])
        return random.choice(weighted)
