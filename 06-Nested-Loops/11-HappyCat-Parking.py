days_count = int(input())
hours_per_day = int(input())
total_price = 0

for d in range(1, days_count + 1):
    day_price = 0
    for h in range(1, hours_per_day + 1):
        if d % 2 == 0 and h % 2 != 0:
            day_price += 2.50
        elif d % 2 != 0 and h % 2 == 0:
            day_price += 1.25
        else:
            day_price += 1

    total_price += day_price
    print(f"Day: {d} - {day_price :.2f} leva")

print(f"Total: {total_price :.2f} leva")