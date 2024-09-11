fuel_type = input()
fuel_amount = float(input())
discount_card = input()

if fuel_type == "Diesel":
    fuel_price = 2.33
    fuel_discount = 0.12 if discount_card == "Yes" else 0
elif fuel_type == "Gasoline":
    fuel_price = 2.22
    fuel_discount = 0.18 if discount_card == "Yes" else 0
elif fuel_type == "Gas":
    fuel_price = 0.93
    fuel_discount = 0.08 if discount_card == "Yes" else 0
else:
    fuel_price = 0
    fuel_discount = 0

final_fuel_price = fuel_price - fuel_discount
total_price = final_fuel_price * fuel_amount

extra_discount = 0
if fuel_amount > 25:
    extra_discount = 10 / 100
elif fuel_amount >= 20:
    extra_discount = 8 / 100

final_total_price = total_price * (1 - extra_discount)

print(f"{final_total_price:.2f} lv.")
