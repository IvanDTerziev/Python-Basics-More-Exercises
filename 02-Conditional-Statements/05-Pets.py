import math

days = int(input())
food_kg = int(input())
dog_food_day = float(input())
cat_food_day = float(input())
food_turtle_grams = float(input()) / 1000

total_food_needed = days * (dog_food_day + cat_food_day + food_turtle_grams)

if total_food_needed <= food_kg:
    print(f"{math.floor(food_kg - total_food_needed)} kilos of food left.")
else:
    print(f"{math.ceil(total_food_needed - food_kg)} more kilos of food are needed.")
