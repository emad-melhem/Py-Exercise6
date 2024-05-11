

#change type from string to int.
def ChangeStrToInt(lst):
    for i, j in enumerate(lst):
        if j.isnumeric():
            lst[i]= int(j)

list_1 = ChangeStrToInt(input("Enter the first set\n"
                    +"'put a space between them' :").split())
list_2 = ChangeStrToInt(input("Enter the second set\n"
                    +"'put a space between them' :").split())

set_1 = set(list_1)
set_2 = set(list_2)

new_dict = {list_1[i]: list_2[i] for i in range(len(list_1))}

print(f'The dictionary is: {new_dict}')