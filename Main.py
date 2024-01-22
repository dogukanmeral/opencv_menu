import cv2
import numpy as np
import time

from capture_frame import capture_frame_to_file
from mask_color import mask_color
from find_shapes import find_shapes
from find_in_menu import find_in_menu
from find_in_menu import find_price

colors_upper_lower_values = {"red": [[0, 10],[160, 179]],
                             "cyan": [80,100],
                             "violet": [110, 130],
                             "chartreuse_green": [45, 65]}


capture_frame_to_file(0, "order.png", "c")

order_image = cv2.imread("order.png")

colors_with_shapes = {}
for color, values in colors_upper_lower_values.items():
	if color == "red":
		masked_image = mask_color(order_image, values[0][0], values[0][1]) + mask_color(order_image, values[1][0], values[1][1])
	else:
		masked_image = mask_color(order_image, values[0], values[1])

	colors_with_shapes[color] = find_shapes(masked_image, 400)

for color, shapes in colors_with_shapes.items():
	if len(shapes) > 1:
		print("only one of the same color object you can select")
		quit()

if len(colors_with_shapes["red"]) + len(colors_with_shapes["violet"]) != 2:
	print("choose at least one main course and one starter to create the menu.")
	quit()

orders = []
for color, shapes in colors_with_shapes.items():
	for num_of_vertices in shapes:
		if find_in_menu(color, num_of_vertices) is not None:
			orders.append(find_in_menu(color, num_of_vertices))

confirmation_str = input(f"Your order is {', '.join(orders)}, do you confirm? (y/n): ")

if confirmation_str in "yY ":
	prices_of_items = [find_price(item) for item in orders]
	print(f"The total amount you have to pay: {sum(prices_of_items)} TL")