
print("A list is created in Python by placing items inside [], separated by commas . For example,")

# A list with 3 integers
numbers = [1, 2, 5]

print(numbers)

# Output: [1, 2, 5]
print("")

print("In Python, each item in a list is associated with a number. The number is known as a list index.We can access elements of an array using the index number (0, 1, 2 …). For example,")

languages = ["Python", "Swift", "C++"]

# access item at index 0
print(languages[0])   # Python

# access item at index 2
print(languages[2])   # C++

print("")
print("Python allows negative indexing for its sequences. The index of -1 refers to the last item, -2 to the second last item and so on.")

languages = ["Python", "Swift", "C++"]

# access item at index 0
print(languages[-1])   # C++

# access item at index 2
print(languages[-3])   # Python

print("")
print("In Python it is possible to access a section of items from the list using the slicing operator :, not just a single item")

# List slicing in Python

my_list = ['p','r','o','g','r','a','m','i','z']

# items from index 2 to index 4
print(my_list[2:5])

# items from index 5 to end
print(my_list[5:])

# items beginning to end
print(my_list[:])

print("")
print("Using append()The append() method adds an item at the end of the list.")

numbers = [21, 34, 54, 12]

print("Before Append:", numbers)

# using append method
numbers.append(32)

print("After Append:", numbers)

print("")
print("Using extend() We use the extend() method to add all items of one list to another.")

prime_numbers = [2, 3, 5]
print("List1:", prime_numbers)

even_numbers = [4, 6, 8]
print("List2:", even_numbers)

# join two lists
prime_numbers.extend(even_numbers)

print("List after append:", prime_numbers)

print("")
print("Python lists are mutable. Meaning lists are changeable. And, we can change items of a list by assigning new values using = operator.")

languages = ['Python', 'Swift', 'C++']

# changing the third item to 'C'
languages[2] = 'C'

print(languages)  # ['Python', 'Swift', 'C']

print("")
print("Remove an Item From a List, Using del() In Python we can use the del statement to remove one or more items from a list.")

languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']

# deleting the second item
del languages[1]
print(languages) # ['Python', 'C++', 'C', 'Java', 'Rust', 'R']

# deleting the last item
del languages[-1]
print(languages) # ['Python', 'C++', 'C', 'Java', 'Rust']

# delete first two items
del languages[0 : 2]  # ['C', 'Java', 'Rust']
print(languages)

print("")
print("Using remove() We can also use the remove() method to delete a list item.")

languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']

# remove 'Python' from the list
languages.remove('Python')

print(languages) # ['Swift', 'C++', 'C', 'Java', 'Rust', 'R']

print("")
print("Iterating through a List")
print("We can use the for loop to iterate over the elements of a list")

languages = ['Python', 'Swift', 'C++']

# iterating through the list
for language in languages:
    print(language)

print("")   
print("Check if an Item Exists in the Python List")
print("We use the in keyword to check if an item exists in the list or not.")

languages = ['Python', 'Swift', 'C++']

print('C' in languages)    # False
print('Python' in languages)    # True

print("")
print("Python List Length")
print("In Python, we use the len() function to find the number of elements present in a list.")


languages = ['Python', 'Swift', 'C++']

print("List: ", languages)

print("Total Elements: ", len(languages))    # 3

print("")
print("Python List Comprehension")
print("List comprehension is a concise and elegant way to create lists.")
print("A list comprehension consists of an expression followed by the for statement inside square brackets.")

numbers = [number*number for number in range(1, 6)]

print(numbers)    

print("------------ End of Lists -------------------")
# Output: [1, 4, 9, 16, 25]




