# 1. List operations
list1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
list2 = [5, 3, 5, 8, 9, 7, 9, 3, 2, 3]

# a) Combine lists
combined = list1 + list2
print("Combined list:", combined)

# b) Remove duplicates
unique_list = list(set(combined))
print("List with duplicates removed:", unique_list)

# c) Sort in descending order
sorted_list = sorted(unique_list, reverse=True)
print("Sorted list (descending):", sorted_list)

# 2. Set of unique characters from a list of words
words = ["python", "programming", "language"]
unique_chars = set(''.join(words))
print("Unique characters:", unique_chars)

# 3. Common elements between two lists without using sets
list3 = [1, 2, 3, 4, 5]
list4 = [4, 5, 6, 7, 8]
common = [x for x in list3 if x in list4]
print("Common elements:", common)

# 4. Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# a) Union
union_set = set1.union(set2)
print("Union:", union_set)

# b) Intersection
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# c) Difference
difference_set = set1.difference(set2)
print("Difference (set1 - set2):", difference_set)

# d) Symmetric difference
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference:", symmetric_difference_set)

# 5. Remove vowels from a string using a set
def remove_vowels(string):
    vowels = set('aeiouAEIOU')
    return ''.join(char for char in string if char not in vowels)

text = "Hello, World!"
print("Text without vowels:", remove_vowels(text))

# 6. Find second largest number
numbers = [5, 2, 8, 1, 9, 3, 7]
second_largest = sorted(set(numbers), reverse=True)[1]
print("Second largest number:", second_largest)