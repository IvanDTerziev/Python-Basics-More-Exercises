control_value = int(input())
result = []

for a in range(1, 10):
    for b in range(1, 10):
        if a >= b:
            continue
        for c in range(1, 10):
            for d in range(1, 10):
                if c <= d:
                    continue
                if a * b + c * d == control_value:
                    result.append(f"{a}{b}{c}{d}")

if result:
    print(" ".join(result))
    if len(result) >= 4:
        print(f"Password: {result[3]}")
    else:
        print("No!")
else:
    print("No!")
