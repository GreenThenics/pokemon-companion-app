from pymongo.collection import Collection
from bson.son import SON
from datetime import datetime


class HistoryModel:
    def __init__(self, db):
        self.collection: Collection = db["history"]

    # Insert new history entry
    def add_history(self, traits, companion):
        self.collection.insert_one({
            "traits": traits,
            "companion": companion.lower(),
            "date": datetime.utcnow()
        })

    # Last 10 entries
    def get_recent(self, limit=10):
        cursor = self.collection.find({}, {"_id": 0}).sort("date", -1).limit(limit)
        return list(cursor)

    # Best Pokémon by trait
    def get_best_by_trait(self):
        pipeline = [
            {"$unwind": "$traits"},
            {"$group": {"_id": {"trait": "$traits", "pokemon": "$companion"}, "count": {"$sum": 1}}},
            {"$sort": SON([("count", -1)])},
            {"$group": {
                "_id": "$_id.trait",
                "topPokemon": {"$first": "$_id.pokemon"},
                "count": {"$first": "$count"}
            }},
            {"$sort": {"_id": 1}}
        ]
        return list(self.collection.aggregate(pipeline))

    # Top combos
    def get_top_combos(self, limit=5):
        pipeline = [
            {"$group": {"_id": "$traits", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": limit}
        ]
        return list(self.collection.aggregate(pipeline))

    # Search by Pokémon
    def search_by_pokemon(self, pokemon_name):
        cursor = self.collection.find({"companion": pokemon_name.lower()}, {"_id": 0}).sort("date", -1)
        results = []
        for doc in cursor:
            if isinstance(doc.get("date"), str):
                try:
                    doc["date"] = datetime.fromisoformat(doc["date"])
                except ValueError:
                    pass
            results.append(doc)
        return results
