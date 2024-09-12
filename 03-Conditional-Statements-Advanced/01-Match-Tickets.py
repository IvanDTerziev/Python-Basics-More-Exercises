budget = float(input())
category = input()
fans_count = int(input())

transport = 0
if fans_count < 4:
    transport = 0.75
elif fans_count < 10:
    transport = 0.60
elif fans_count < 25:
    transport = 0.50
elif fans_count < 50:
    transport = 0.40
else:
    transport = 0.25

ticket_price = 0
if category == "VIP":
    ticket_price = 499.99
elif category == "Normal":
    ticket_price = 249.99

available_money = budget * (1 - transport)
needed_money = fans_count * ticket_price

if available_money >= needed_money:
    print(f"Yes! You have {available_money - needed_money :.2f} leva left.")
else:
    print(f"Not enough money! You need {needed_money - available_money :.2f} leva.")