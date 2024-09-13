money = float(input())
end = int(input())
age = 18
money_needed = 0

for y in range(1800, end + 1):
    if y % 2 == 0:
        money_needed += 12000
    else:
        money_needed += 12000 + 50 * age
    age += 1

if money >= money_needed:
    print(f"Yes! He will live a carefree life and will have {money - money_needed :.2f} dollars left.")
else:
    print(f"He will need {money_needed - money:.2f} dollars to survive.")
