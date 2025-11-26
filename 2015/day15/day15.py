# https://adventofcode.com/2015/day/15

import re
import itertools
from collections import defaultdict

def parse_input():
    with open("2015/day15/input.txt", "r") as f:
        ingredients = {}
        for l in f.readlines():
            match = re.match(r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)", l.strip())
            ingredients[match.group(1)] = {
                'capacity': int(match.group(2)),
                'durability': int(match.group(3)),
                'flavor': int(match.group(4)),
                'texture': int(match.group(5)),
                'calories': int(match.group(6))
            }
        return ingredients

def calculate_score(ingredients, amounts):
    total_capacity = sum(ingredients[name]['capacity'] * amount for name, amount in amounts.items())
    total_durability = sum(ingredients[name]['durability'] * amount for name, amount in amounts.items())
    total_flavor = sum(ingredients[name]['flavor'] * amount for name, amount in amounts.items())
    total_texture = sum(ingredients[name]['texture'] * amount for name, amount in amounts.items())
    
    return max(0, total_capacity) * max(0, total_durability) * max(0, total_flavor) * max(0, total_texture)

def find_best_recipe(ingredients, total_amount=100):
    best_score = 0
    best_combination = None
    
    ingredient_names = list(ingredients.keys())
    
    for amounts in itertools.product(range(total_amount + 1), repeat=len(ingredient_names)):
        if sum(amounts) != total_amount:
            continue
        
        amounts_dict = dict(zip(ingredient_names, amounts))
        score = calculate_score(ingredients, amounts_dict)
        
        if score > best_score:
            best_score = score
            best_combination = amounts_dict
            
    return best_score, best_combination

def find_best_recipe_with_calories(ingredients, total_amount=100, target_calories=500):
    best_score = 0
    best_combination = None
    
    ingredient_names = list(ingredients.keys())
    
    for amounts in itertools.product(range(total_amount + 1), repeat=len(ingredient_names)):
        if sum(amounts) != total_amount:
            continue
        
        amounts_dict = dict(zip(ingredient_names, amounts))
        total_calories = sum(ingredients[name]['calories'] * amount for name, amount in amounts_dict.items())
        
        if total_calories != target_calories:
            continue
        
        score = calculate_score(ingredients, amounts_dict)
        
        if score > best_score:
            best_score = score
            best_combination = amounts_dict
            
    return best_score, best_combination

ingredients = parse_input()

# Part 1
best_score, best_combination = find_best_recipe(ingredients)
print(best_score)

# Part 2
best_score_calories, best_combination_calories = find_best_recipe_with_calories(ingredients)
print(best_score_calories)
