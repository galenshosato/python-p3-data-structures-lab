spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_names = [value["name"] for value in spicy_foods]
    return spicy_names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [value for value in spicy_foods if value["heat_level"] > 5]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for item in spicy_foods:
        item_name = item["name"]
        item_cuisine = item["cuisine"]
        item_heat = int(item["heat_level"]) * '🌶' 
        print(f"{item_name} ({item_cuisine}) | Heat Level: {item_heat}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    for item in spicy_foods:
        item_name = item["name"]
        item_cuisine = item["cuisine"]
        item_heat = int(item["heat_level"]) * '🌶'
        if item["heat_level"] > 5: 
            print(f"{item_name} ({item_cuisine}) | Heat Level: {item_heat}")

def get_average_heat_level(spicy_foods):
    avg = [value["heat_level"] for value in spicy_foods]
    i = 0
    n = 0
    while i < len(avg):
        n = n + avg[i]
        i += 1
    return n / len(avg)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
