menu = {"red": {3: "soup", 4: "cheese platter", 5: "garlic bread"},
		"cyan": {3: "crispy chicken", 4: "fish and chips", 5: "omelette"},
		"violet": {3: "meatballs", 4: "casseroles", 5: "fajitas"},
		"chartreuse_green": {3: "souffle", 4: "tiramisu", 5: "cheesecake"}}

prices = {"soup": 54,
          "cheese platter": 21,
          "garlic bread": 42,
          "crispy chicken": 76,
          "fish and chips": 87,
          "omelette": 43,
          "meatballs": 89,
          "casseroles": 94,
          "fajitas": 28,
          "souffle": 19,
          "tiramisu": 81,
          "cheesecake": 28}

def find_in_menu(color, num_of_vertices):
	global menu

	if color not in menu or num_of_vertices not in menu[color]:
		return None
	else:
		return menu[color][num_of_vertices]

def find_price(item):
	global prices

	return prices[item]