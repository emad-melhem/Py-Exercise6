
# exercise 3.1
red_objects ={"apple", "crab", "rose", "strawberry"}
fruits = {"orange", "apple", "strawberry", "grape", "kiwi", "mandarin"}

print(f"the red fruits is {fruits & red_objects}")
print(f"all fruits that aren’t red fruits is {fruits - red_objects}")


# exercise 3.2
orange_objects ={"basketball", "fanta", "orange", "autumn leaves", "mandarin"}

print(f"all of the red and orange fruits but none of the other ones is {fruits & (red_objects | orange_objects)}")
print(f"all of the objects without the fruits is {(red_objects | orange_objects) - fruits}")


# exercise 3.2
print(f"all of the objects and fruits is {list(red_objects | orange_objects | fruits)}")