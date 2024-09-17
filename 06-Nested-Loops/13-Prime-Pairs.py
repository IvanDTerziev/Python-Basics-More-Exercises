starting_for_first_pair = int(input())
starting_for_second_pair = int(input())
ending_for_first_pair = int(input())
ending_for_second_pair = int(input())

results = []

for f in range(starting_for_first_pair, starting_for_first_pair + ending_for_first_pair + 1):
    for s in range(starting_for_second_pair, starting_for_second_pair + ending_for_second_pair + 1):
        first_part_prime = True
        second_part_prime = True

        for divisor in range(2, f):
            if f % divisor == 0:
                first_part_prime = False
                break

        for divisor in range(2, s):
            if s % divisor == 0:
                second_part_prime = False
                break

        if first_part_prime and second_part_prime and f != 1 and s != 1:
            current_number = f * 100 + s
            results.append(current_number)

print(*results, sep="\n")
