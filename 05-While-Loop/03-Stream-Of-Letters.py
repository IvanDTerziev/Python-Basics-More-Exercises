c_count = 0
o_count = 0
n_count = 0

result_string = ""
current_string = ""

command = input()

while command != "End":
    if not command.isalpha():
        command = input()
        continue

    if command == "c" and c_count == 0:
        c_count += 1
    elif command == "o" and o_count == 0:
        o_count += 1
    elif command == "n" and n_count == 0:
        n_count += 1
    else:
        current_string += command

    if c_count == 1 and o_count == 1 and n_count == 1:
        result_string += f"{current_string} "
        current_string = ""
        c_count = 0
        o_count = 0
        n_count = 0

    command = input()

print(result_string)
