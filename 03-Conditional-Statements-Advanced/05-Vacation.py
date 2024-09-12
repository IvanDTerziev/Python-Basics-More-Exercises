camp_options = [("Summer", "Alaska", 0.65), ("Winter", "Morocco", 0.45)]
hut_options = [("Summer", "Alaska", 0.80), ("Winter", "Morocco", 0.60)]
hotel_options = [("Summer", "Alaska", 0.90), ("Winter", "Morocco", 0.90)]

stay_options = [
    ("Camp", camp_options),
    ("Hut", hut_options),
    ("Hotel", hotel_options)
]

budget = float(input())
season = input()

if budget <= 1000:
    selected_stay = stay_options[0]
elif budget <= 3000:
    selected_stay = stay_options[1]
else:
    selected_stay = stay_options[2]

stay_type = selected_stay[0]

for season_data in selected_stay[1]:
    if season_data[0] == season:
        stay_location = season_data[1]
        stay_price = season_data[2] * budget
        break

print(f"{stay_location} - {stay_type} - {stay_price:.2f}")
