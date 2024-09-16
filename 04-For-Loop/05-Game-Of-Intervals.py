UPPER_BOUNDARY = 50
LOWER_BOUNDARY = 0

counts = [0] * 5
invalid_count = 0
total_score = 0

moves = int(input())

for _ in range(moves):
    current_move = int(input())
    if not (LOWER_BOUNDARY <= current_move <= UPPER_BOUNDARY):
        invalid_count += 1
        total_score /= 2
    elif current_move > 39:
        counts[4] += 1
        total_score += 100
    elif current_move > 29:
        counts[3] += 1
        total_score += 50
    elif current_move > 19:
        counts[2] += 1
        total_score += current_move * 0.40
    elif current_move > 9:
        counts[1] += 1
        total_score += current_move * 0.30
    else:
        counts[0] += 1
        total_score += current_move * 0.20

print(f"{total_score :.2f}")
print(f"From 0 to 9: {counts[0] / moves :.2%}")
print(f"From 10 to 19: {counts[1] / moves :.2%}")
print(f"From 20 to 29: {counts[2] / moves :.2%}")
print(f"From 30 to 39: {counts[3] / moves :.2%}")
print(f"From 40 to 50: {counts[4] / moves :.2%}")
print(f"Invalid numbers: {invalid_count / moves :.2%}")
