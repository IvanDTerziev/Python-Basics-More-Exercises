stadium_capacity = int(input())
all_fans = int(input())

sectors_count = {"A": 0, "B": 0, "V": 0, "G": 0}

for _ in range(all_fans):
    current_sector = input()
    if current_sector in sectors_count:
        sectors_count[current_sector] += 1

sector_a_percent = sectors_count["A"] / all_fans * 100
sector_b_percent = sectors_count["B"] / all_fans * 100
sector_v_percent = sectors_count["V"] / all_fans * 100
sector_g_percent = sectors_count["G"] / all_fans * 100

all_fans_percent = all_fans / stadium_capacity * 100

print(f"{sector_a_percent:.2f}%")
print(f"{sector_b_percent:.2f}%")
print(f"{sector_v_percent:.2f}%")
print(f"{sector_g_percent:.2f}%")
print(f"{all_fans_percent:.2f}%")
