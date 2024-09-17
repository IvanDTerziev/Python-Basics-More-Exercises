n = int(input())
l = int(input())

result = []

for first in range(1, n + 1):
    for s in range(1, n + 1):
        for t in range(97, 97 + l):
            for f in range(97, 97 + l):
                for fifth in range(1, n + 1):
                    if fifth > max(first, s):
                        result.append(f"{first}{s}{chr(t)}{chr(f)}{fifth}")

print(" ".join(result))
