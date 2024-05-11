my_dict = {0: 19, 1: 33, 2: 18, 3: 30, 4: 26}

order_keys = sorted(my_dict.keys())
order_values = sorted(my_dict.values())

new_dict = dict()
for i in range(len(order_keys)):
    new_dict.update({order_keys[i] : order_values[i]})

print(f"The sorted dictionary is: {new_dict}")