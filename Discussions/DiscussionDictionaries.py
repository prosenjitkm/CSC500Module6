"""
Dictionaries
Key-value pairs where each key is unique.
Perfect for when you need to map items, like names to grades.
Inserting Elements:
Use assignment to add new items.
update(): Add multiple items at once.
"""
grades = {"Alice": 85, "Bob": 92}
grades["Charlie"] = 88
grades.update({"Diana": 90, "Eve": 95})
print(grades)
"""
Updating Elements:
Use assignment to change a value.
"""
grades["Alice"] = 89
print(grades)

"""
Removing Elements:
pop(key): Removes a key and returns its value.
popitem(): Removes the last added item.
del: Deletes a key.
clear(): Removes all items.
"""
grades.pop("Bob")
last_item = grades.popitem()
del grades["Alice"]
print(grades)

"""
When to Use Lists vs. Dictionaries
>We use Lists when:
>>You need an ordered collection.
>>You access elements by their position.

>Use Dictionaries when:
>>You need to map unique keys to values.
>>Quick lookups by key are important.

Example:
List: Store student names: ["Alice", "Bob", "Charlie"]
Dictionary: Store student grades: {"Alice": 85, "Bob": 92}
"""