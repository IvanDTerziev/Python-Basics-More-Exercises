WATER_BILL_PER_MONTH = 20
INTERNET_BILL_PER_MONTH = 15
OTHER_BILLS_PER_MONTH_MULTIPLIER = 1.20

bills_total = [0, 0, 0, 0]

months_count = int(input())

for _ in range(months_count):
    electricity_bill = float(input())
    bills_total[0] += electricity_bill
    bills_total[1] += WATER_BILL_PER_MONTH
    bills_total[2] += INTERNET_BILL_PER_MONTH
    bills_total[3] += OTHER_BILLS_PER_MONTH_MULTIPLIER * \
                      (WATER_BILL_PER_MONTH + INTERNET_BILL_PER_MONTH + electricity_bill)

total_bills = sum(bills_total)

print(f"Electricity: {bills_total[0] :.2f} lv")
print(f"Water: {bills_total[1] :.2f} lv")
print(f"Internet: {bills_total[2] :.2f} lv")
print(f"Other: {bills_total[3] :.2f} lv")
print(f"Average: {total_bills / months_count :.2f} lv")
