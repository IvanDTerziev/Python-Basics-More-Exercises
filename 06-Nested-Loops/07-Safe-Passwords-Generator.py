a = int(input())
b = int(input())
max_generated_passwords = int(input())

A = 35
B = 64
passwords = []

for x in range(1, a + 1):
    for y in range(1, b + 1):
        password = f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}"
        passwords.append(password)

        A = 35 if A + 1 > 55 else A + 1
        B = 64 if B + 1 > 96 else B + 1

        if len(passwords) >= max_generated_passwords:
            print("|".join(passwords) + "|")
            exit()

print("|".join(passwords) + "|")
