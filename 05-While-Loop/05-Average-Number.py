numbers = int(input())
total_sum = 0
for i in range(numbers):
    total_sum += int(input())

print(f"{total_sum / numbers:.2f}")
