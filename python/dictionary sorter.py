def sort_dictionaries(dict_list, sort_key):
    return sorted(dict_list, key=lambda x: x[sort_key])

# Example list of dictionaries
people = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"},
    {"name": "David", "age": 28, "city": "Boston"}
]

print("Original list:")
for person in people:
    print(person)

# Sort by age
sorted_by_age = sort_dictionaries(people, "age")
print("\nSorted by age:")
for person in sorted_by_age:
    print(person)

# Sort by name
sorted_by_name = sort_dictionaries(people, "name")
print("\nSorted by name:")
for person in sorted_by_name:
    print(person)

# Sort by city
sorted_by_city = sort_dictionaries(people, "city")
print("\nSorted by city:")
for person in sorted_by_city:
    print(person)