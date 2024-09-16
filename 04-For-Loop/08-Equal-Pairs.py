n = int(input())
current_sum = int(input()) + int(input())
diff_sum = 0

for _ in range(n - 1):
    next_sum = int(input()) + int(input())
    current_diff = abs(current_sum - next_sum)

    if current_diff > diff_sum:
        diff_sum = current_diff

    current_sum = next_sum

if diff_sum == 0:
    print(f"Yes, value={current_sum}")
else:
    print(f"No, maxdiff={diff_sum}")
