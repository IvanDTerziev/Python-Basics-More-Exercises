weather = float(input())

if weather < 5 or weather > 35:
    print("unknown")
elif weather >= 26:
    print("Hot")
elif weather > 20:
    print("Warm")
elif weather >= 15:
    print("Mild")
elif weather >= 12:
    print("Cool")
else:
    print("Cold")