start_digit = int(input())
end_digit = int(input())

result = []

for first in range(start_digit, end_digit + 1):
    for second in range(start_digit, end_digit + 1):
        for third in range(start_digit, end_digit + 1):
            for forth in range(start_digit, end_digit + 1):
                if (first % 2 == 0 and forth % 2 == 0) or (first % 2 != 0 and forth % 2 != 0):
                    continue
                if first < forth:
                    continue
                if (second + third) % 2 != 0:
                    continue

                result.append(1000 * first + 100 * second + 10 * third + 1 * forth)

print(' '.join(map(str, result)))
