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
    names_list = []
    for food in spicy_foods:
        names_list.append(food["name"])
    return names_list


def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_foods


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        emoji_string = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {emoji_string}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    filtered_spicy_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(filtered_spicy_foods)


def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    for food in spicy_foods:
        total_heat_level += food["heat_level"]
    get_average_heat_level = total_heat_level / len(spicy_foods)
    return int(get_average_heat_level)
    

def create_spicy_food(spicy_foods, spicy_food):
    updated_spicy_foods = spicy_foods + [spicy_food]
    return updated_spicy_foods
