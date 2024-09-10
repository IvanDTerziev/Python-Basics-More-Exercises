house_height = float(input())
house_length = float(input())
roof_height = float(input())

front_back_wall_area = house_height * house_height
door_area = 1.2 * 2
front_back_wall_paint_area = 2 * front_back_wall_area - door_area

side_wall_area = house_height * house_length
window_area = 1.5 * 1.5
side_walls_paint_area = 2 * (side_wall_area - window_area)

total_green_paint_area = front_back_wall_paint_area + side_walls_paint_area
total_green_paint_needed = total_green_paint_area / 3.4

roof_rectangle_area = 2 * (house_height * house_length)
roof_triangle_area = 2 * (house_height * roof_height / 2)
total_red_paint_area = roof_rectangle_area + roof_triangle_area
total_red_paint_needed = total_red_paint_area / 4.3

print(f"{total_green_paint_needed:.2f}")
print(f"{total_red_paint_needed:.2f}")
