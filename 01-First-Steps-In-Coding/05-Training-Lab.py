hallway = 100
desk_size = 70
row_size = 120
door_size_as_desks = 3

length = float(input()) * 100
width = float(input()) * 100

useful_width = width - hallway

desks_per_row = useful_width // desk_size
rows = length // row_size

desks = int(rows * desks_per_row - door_size_as_desks)
print(desks)
