tons_of_bus = 0
tons_of_truck = 0
tons_of_train = 0

cargo = int(input())

for _ in range(cargo):
    current_cargo = int(input())
    if current_cargo <= 3:
        tons_of_bus += current_cargo
    elif current_cargo <= 11:
        tons_of_truck += current_cargo
    else:
        tons_of_train += current_cargo

total_tons = tons_of_bus + tons_of_truck + tons_of_train

total_money = tons_of_bus * 200 + tons_of_truck * 175 + tons_of_train * 120
average_money = total_money / total_tons

print(f"{average_money :.2f}")
print(f"{tons_of_bus / total_tons :.2%}")
print(f"{tons_of_truck / total_tons :.2%}")
print(f"{tons_of_train / total_tons :.2%}")