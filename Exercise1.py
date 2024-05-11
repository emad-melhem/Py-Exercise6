

set_1 = {1, 2, 3, 4}
set_2 =  {7, 8, 9, 10}

list_1 = list(set_1)
list_2 = list(set_2)
list_1.sort()
list_2.sort()

new_dict = {list_1[i]: list_2[i] for i in range(len(list_1))}

print(f'The dictionary is: {new_dict}')