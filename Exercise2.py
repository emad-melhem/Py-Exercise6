my_dict = {"fruit": "Apple", "vegetable": "Capsicum"}

key= input("Enter a word to check it in the dictionary :")
find_letter = False
for x in my_dict.keys():
    if key.lower() == x.lower():
        find_letter =True
        break
if find_letter:
    print(f"{key} is in the dictionary!")
else:
    my_dict.update({key: 'empty'})
    print(f"{key} is not in the dictionary! \nThe new dictionary is: {my_dict}")