DISHWASHER_DETERGENT_ML = 750
DISH_NEEDED_ML = 5
POT_NEEDED_ML = 15
END_COMMAND = "End"

detergent_ml = int(input()) * DISHWASHER_DETERGENT_ML

loads = {'dishes': 0, 'pots': 0}
current_load = 0

while True:
    command = input()
    if command == END_COMMAND:
        break
    current_load += 1

    if current_load % 3 == 0:
        loads['pots'] += int(command)
        detergent_ml -= int(command) * POT_NEEDED_ML
    else:
        loads['dishes'] += int(command)
        detergent_ml -= int(command) * DISH_NEEDED_ML

    if detergent_ml < 0:
        break

if detergent_ml >= 0:
    print("Detergent was enough!")
    print(f"{loads['dishes']} dishes and {loads['pots']} pots were washed.")
    print(f"Leftover detergent {detergent_ml} ml.")
else:
    print(f"Not enough detergent, {-detergent_ml} ml. more necessary!")
