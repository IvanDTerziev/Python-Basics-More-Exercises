pay_per_km = {
    "Spring": [0.75, 0.95, 1.45],
    "Summer": [0.90, 1.10, 1.45],
    "Autumn": [0.75, 0.95, 1.45],
    "Winter": [1.05, 1.25, 1.45],
}

season = input()
km = float(input())

if km <= 5000:
    pay_per_km_selected = pay_per_km[season][0]
elif km <= 10000:
    pay_per_km_selected = pay_per_km[season][1]
else:
    pay_per_km_selected = pay_per_km[season][2]

total_income = km * pay_per_km_selected * 4
net_income = total_income * (1 - 10 / 100)

print(f"{net_income:.2f}")
