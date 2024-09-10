veg_price = float(input())
fruit_price = float(input())
veg_kg = int(input())
fruit_kg = int(input())

fruits = veg_price * veg_kg
vegetables = fruit_price * fruit_kg

total_sum = fruits + vegetables
total_sum_in_euro = total_sum / 1.94

print(f"{total_sum_in_euro:.2f}")
