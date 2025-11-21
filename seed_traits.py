from pymongo import MongoClient
from config import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db["traits_mapping"]

# sample = [
#     {"trait": "brave", "pokemon": ["charizard", "lucario", "blaziken", "gallade"]},
#     {"trait": "loyal", "pokemon": ["pikachu", "eevee", "snorlax", "lucario"]},
#     {"trait": "funny", "pokemon": ["jigglypuff", "psyduck", "sliggoo", "minun"]},
#     {"trait": "calm", "pokemon": ["lapras", "vaporeon", "snorlax", "slowpoke"]},
#     {"trait": "energetic", "pokemon": ["pichu", "raichu", "scorbunny", "jitters"]},
#     {"trait": "curious", "pokemon": ["porygon", "psyduck", "alakazam", "eevee"]},
#     {"trait": "stubborn", "pokemon": ["bulbasaur", "mudkip", "snorlax", "aron"]},
#     {"trait": "playful", "pokemon": ["togepi", "clefairy", "pikachu", "piplup"]},
#     {"trait": "smart", "pokemon": ["alakazam", "metagross", "gabite", "porygon"]},
#     {"trait": "shy", "pokemon": ["scyther", "mime-jr", "munna", "espurr"]},
# ]

# collection.delete_many({})
# collection.insert_many(sample)
# print("Seeded traits_mapping with sample data.")

sample = [
    {"trait": "brave", "pokemon": [
        "charizard", "lucario", "blaziken", "gallade", "infernape",
        "machamp", "heracross", "garchomp", "braviary", "emboar",
        "houndoom", "salamence", "lycanroc", "sirfetchd", "primeape",
        "aegislash", "scizor", "rhyperior", "terrakion", "kommo-o"
    ]},
    {"trait": "loyal", "pokemon": [
        "pikachu", "eevee", "snorlax", "lucario", "arcanine",
        "houndoom", "growlithe", "ninetales", "umbreon", "espeon",
        "silicobra", "mudsdale", "boltund", "zamazenta", "milotic",
        "altaria", "togekiss", "manectric", "rapidash", "lapras"
    ]},
    {"trait": "funny", "pokemon": [
        "jigglypuff", "psyduck", "sliggoo", "minun", "ludicolo",
        "mr-mime", "ditto", "wobbuffet", "bidoof", "spinda",
        "trubbish", "swalot", "octillery", "dunsparce", "whismur",
        "chatot", "alomomola", "sudowoodo", "quagsire", "slurpuff"
    ]},
    {"trait": "calm", "pokemon": [
        "lapras", "vaporeon", "snorlax", "slowpoke", "togekiss",
        "altaria", "milotic", "suicune", "cresselia", "gardevoir",
        "mesprit", "jirachi", "uxie", "musharna", "drampa",
        "slowking", "bellossom", "audino", "lumineon", "gothitelle"
    ]},
    {"trait": "energetic", "pokemon": [
        "pichu", "raichu", "scorbunny", "jitters", "torchic",
        "electrike", "manectric", "blitzle", "zebstrika", "helioptile",
        "heliolisk", "plusle", "minun", "emboar", "thundurus",
        "zeraora", "pikipek", "talonflame", "luxray", "rotom"
    ]},
    {"trait": "curious", "pokemon": [
        "porygon", "psyduck", "alakazam", "eevee", "rotom",
        "celebi", "jirachi", "solosis", "reuniclus", "hoopa",
        "elgyem", "beheeyem", "munna", "musharna", "spoink",
        "grumpig", "chingling", "chingling", "mimikyu", "espurr"
    ]},
    {"trait": "stubborn", "pokemon": [
        "bulbasaur", "mudkip", "snorlax", "aron", "rhydon",
        "torkoal", "steelix", "golem", "gigalith", "pangoro",
        "torterra", "donphan", "conkeldurr", "gurdurr", "croagunk",
        "toxicroak", "scraggy", "scrafty", "druddigon", "crustle"
    ]},
    {"trait": "playful", "pokemon": [
        "togepi", "clefairy", "pikachu", "piplup", "plusle",
        "mime-jr", "azurill", "bonsly", "happiny", "panpour",
        "pansage", "pansear", "oshawott", "popplio", "squirtle",
        "fennekin", "rowlet", "chikorita", "tepig", "grookey"
    ]},
    {"trait": "smart", "pokemon": [
        "alakazam", "metagross", "gabite", "porygon", "gardevoir",
        "beheeyem", "slowking", "mewtwo", "jirachi", "latios",
        "latias", "espeon", "uxie", "solgaleo", "necrozma",
        "rotom", "magnezone", "oranguru", "hoopa", "claydol"
    ]},
    {"trait": "shy", "pokemon": [
        "scyther", "mime-jr", "munna", "espurr", "abra",
        "ralts", "banette", "shedinja", "zorua", "gothita",
        "gothorita", "togetic", "snorunt", "froslass", "misdreavus",
        "drifloon", "phantump", "pumpkaboo", "yamask", "sandygast"
    ]},
]

for entry in sample:
    collection.update_one({"trait": entry["trait"]}, {"$set": {"pokemon": entry["pokemon"]}}, upsert=True)
print("Traits updated with 20 Pokémon each!")