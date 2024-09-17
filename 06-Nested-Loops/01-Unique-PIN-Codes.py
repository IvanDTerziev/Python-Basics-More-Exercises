first_digit_boundary = int(input())
second_digit_boundary = int(input())
third_digit_boundary = int(input())

for first in range(1, first_digit_boundary + 1):
    for second in range(1, second_digit_boundary + 1):
        for third in range(1, third_digit_boundary + 1):
            if first % 2 == 0:
                is_prime = True
                if second == 1:
                    is_prime = False
                else:
                    for divisor in range(2, second):
                        if second % divisor == 0:
                            is_prime = False
                            break

                if is_prime and third % 2 == 0:
                    print(f"{first} {second} {third}")
