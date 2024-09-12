prices_and_sports = {
    "boys": [("Winter", 9.60, "Judo"), ("Spring", 7.20, "Tennis"), ("Summer", 15.00, "Football")],
    "girls": [("Winter", 9.60, "Gymnastics"), ("Spring", 7.20, "Athletics"), ("Summer", 15.00, "Volleyball")],
    "mixed": [("Winter", 10.00, "Ski"), ("Spring", 9.50, "Cycling"), ("Summer", 20.00, "Swimming")]
}

season = input()
group_type = input()
group_count = int(input())
nights = int(input())

for s, price, sport in prices_and_sports[group_type]:
    if s == season:
        price_per_night = price
        sport_type = sport
        break

if group_count >= 50:
    discount = 0.50
elif group_count >= 20:
    discount = 0.15
elif group_count >= 10:
    discount = 0.05
else:
    discount = 0.00

price_per_night *= (1 - discount)
total_price = price_per_night * nights * group_count

print(f"{sport_type} {total_price:.2f} lv.")
