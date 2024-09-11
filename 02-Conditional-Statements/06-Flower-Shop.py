import math

magnolias_count = int(input())
hyacinths_count = int(input())
roses_count = int(input())
cacti_count = int(input())
gift_price = float(input())

total_income = magnolias_count * 3.25 + \
               hyacinths_count * 4.00 + \
               roses_count * 3.50 + \
               cacti_count * 8.00

total_income_after_taxes = total_income * (1 - 5 / 100)

if total_income_after_taxes >= gift_price:
    print(f"She is left with {math.floor(total_income_after_taxes - gift_price)} leva.")
else:
    print(f"She will have to borrow {math.ceil(gift_price - total_income_after_taxes)} leva.")