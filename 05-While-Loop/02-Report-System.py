SUCCESSFUL_TRANSACTION_MSG = "Product sold!"
FAILED_TRANSACTION_MSG = "Error in transaction!"
END_COMMAND = "End"

money_totals = [0, 0, 0]
buyers_counts = [0, 0]
current_buyer = 0
is_success = False

money_target = int(input())

command = input()
while command != END_COMMAND:
    current_money = int(command)
    current_buyer += 1

    if (current_money < 10 and current_buyer % 2 == 0) or (current_money > 100 and current_buyer % 2 != 0):
        print(FAILED_TRANSACTION_MSG)
    else:
        money_totals[2] += current_money

        if current_buyer % 2 == 0:
            money_totals[1] += current_money
            buyers_counts[1] += 1
        else:
            money_totals[0] += current_money
            buyers_counts[0] += 1

        print(SUCCESSFUL_TRANSACTION_MSG)

        if money_totals[2] >= money_target:
            is_success = True
            break

    command = input()

if is_success:
    average_cs = money_totals[0] / buyers_counts[0] if buyers_counts[0] > 0 else 0
    average_cc = money_totals[1] / buyers_counts[1] if buyers_counts[1] > 0 else 0
    print(f"Average CS: {average_cs:.2f}")
    print(f"Average CC: {average_cc:.2f}")
else:
    print("Failed to collect required money for charity.")
