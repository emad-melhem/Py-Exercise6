

list_1 = [1, 2, 3, 4]
list_2 = [7, 8, 9, 10]

set_1 = set(list_1)
set_2 =  set(list_2)

new_dict = {list_1[i]: list_2[i] for i in range(len(list_1))}

print(f'The dictionary is: {new_dict}')