"""
Lists
Ordered collections that can contain duplicates.
Ideal when you need to maintain order or access items by their position (index).
Inserting Elements:
append(): Add to the end of the list.
insert(index, value): Add at a specific position.
extend(): Add multiple items.
"""
fruits = ["apple", "banana"]
fruits.append("cherry")
fruits.insert(1, "orange")
fruits.extend(["grape", "mango"])
print(fruits)

"""
Updating Elements:
Use index to update an element.
"""
fruits[0] = "strawberry"
print(fruits)

"""
Removing Elements:
remove(value): Removes the first occurrence.
pop(index): Removes and returns an item at a specific index.
del: Deletes by index.
clear(): Removes all items.
"""
fruits.remove("banana")
removed = fruits.pop(2)
del fruits[0]
print(fruits)
