distance = int(input())
day_or_night = input()
min_price = 0

if distance < 20:
    if day_or_night == "day":
        min_price = 0.70 + 0.79 * distance
    elif day_or_night == "night":
        min_price = 0.70 + 0.90 * distance
elif distance < 100:
    min_price = 0.09 * distance
else:
    min_price = 0.06 * distance

print(f"{min_price:.2f}")
