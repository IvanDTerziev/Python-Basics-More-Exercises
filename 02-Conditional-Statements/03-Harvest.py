from math import floor, ceil

area = int(input())
grapes_per_meter = float(input())
needed_litres = int(input())
workers = int(input())

available_area = 0.4 * area
grapes_for_litre = 2.5
total_grapes = available_area * grapes_per_meter
wine_produced = total_grapes / grapes_for_litre

if wine_produced < needed_litres:
    needed_wine = needed_litres - wine_produced
    print(f"It will be a tough winter! More {floor(needed_wine)} liters wine needed.")
else:
    leftover = wine_produced - needed_litres
    per_person = leftover / workers
    print(f"Good harvest this year! Total wine: {floor(wine_produced)} liters.")
    print(f"{ceil(leftover)} liters left -> {ceil(per_person)} liters per person.")
