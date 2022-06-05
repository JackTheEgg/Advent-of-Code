from collections import defaultdict
from queue import Queue
from math import ceil

def build_ingredient(string):
    parts = string.split(" ")
    return {"ingredient": parts[1], "amount": int(parts[0])}

def build_recipes(data):
    recipes = {}
    for line in data:
        input_str, output_str = line.split(" => ")
        
        ingredients = []
        for ingredient_str in input_str.split(', '):
            ingredients.append(build_ingredient(ingredient_str))
            
        output = build_ingredient(output_str)
        
        recipes[output["ingredient"]] = {
            "servings": output["amount"],
            "ingredients": ingredients
        }
    return recipes

def make_fuel(amount, recipes):
    supply = defaultdict(int)
    orders = Queue()
    orders.put({"ingredient": "FUEL", "amount": amount})
    ore_needed = 0
    while not orders.empty():
        order = orders.get()
        if order["ingredient"] == "ORE":
            ore_needed += order["amount"]
        elif order["amount"] <= supply[order["ingredient"]]:
            supply[order["ingredient"]] -= order["amount"]
        else:
            amount_needed = order["amount"] - supply[order["ingredient"]]
            recipe = recipes[order["ingredient"]]
            batches = ceil(amount_needed / recipe["servings"])
            for ingredient in recipe["ingredients"]:
                orders.put({"ingredient": ingredient["ingredient"], "amount": ingredient["amount"] * batches})
            leftover_amount = batches * recipe["servings"] - amount_needed
            supply[order["ingredient"]] = leftover_amount
    return ore_needed

with open("14.txt") as f:
    data = [row.strip() for row in f.readlines()]

recipes = build_recipes(data)
print(make_fuel(1, recipes))

upper_bound = None
lower_bound = 1
ore_capacity = 1000000000000
recipes = build_recipes(data)
while lower_bound + 1 != upper_bound:
    if upper_bound is None:
        guess = lower_bound * 2
    else:
        guess = (upper_bound + lower_bound) // 2    
    ore_needed = make_fuel(guess, recipes)
    if ore_needed > ore_capacity:
        upper_bound = guess
    else:
        lower_bound = guess
print(lower_bound)