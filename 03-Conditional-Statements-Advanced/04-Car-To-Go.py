economy_class = [("Summer", "Cabrio", 0.35), ("Winter", "Jeep", 0.65)]
compact_class = [("Summer", "Cabrio", 0.45), ("Winter", "Jeep", 0.80)]
luxury_class = [("Summer", "Jeep", 0.90), ("Winter", "Jeep", 0.90)]

car_classes = [
    ("Economy class", economy_class),
    ("Compact class", compact_class),
    ("Luxury class", luxury_class)
]

budget = float(input())
season = input()

if budget <= 100:
    selected_class = car_classes[0]
elif budget <= 500:
    selected_class = car_classes[1]
else:
    selected_class = car_classes[2]

car_class = selected_class[0]

car_type, car_price = next(
    (season_data[1], season_data[2] * budget)
    for season_data in selected_class[1]
    if season_data[0] == season
)

print(car_class)
print(f"{car_type} - {car_price:.2f}")
