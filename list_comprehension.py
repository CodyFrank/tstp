input_string = "Buy 1 get 2 free"

new_list = [c for c in input_string if c.isdigit()][-1]

print(new_list)
