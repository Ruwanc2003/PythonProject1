print("Create a dictionary in Python.")
capital_city = {"Nepal": "Kathmandu", "Italy": "Rome", "England": "London"}
print(capital_city)

print("")
print("Dictionary with keys and values of different data types")
numbers = {1: "One", 2: "Two", 3: "Three"}
print(numbers)

print("")
print("Add Elements to a Python Dictionary")
capital_city = {"Nepal": "Kathmandu", "England": "London"}
print("Initial Dictionary: ",capital_city)

capital_city["Japan"] = "Tokyo"

print("Updated Dictionary: ",capital_city)

print("")
print("Change Value of Dictionary")
student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
print("Initial Dictionary: ", student_id)

student_id[112] = "Stan"

print("Updated Dictionary: ", student_id)

print("")
print("Accessing Elements from Dictionary")
student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}

print(student_id[111])  # prints Eric
print(student_id[113])  # prints Butters

print("")
print("Removing elements from Dictionary")

student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}

print("Initial Dictionary: ", student_id)

del student_id[111]

print("Updated Dictionary ", student_id)

print("")
print("Dictionary Membership Test")

# Membership Test for Dictionary Keys
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# Output: True
print(1 in squares) # prints True

print(2 not in squares) # prints True

# membership tests for key only not value
print(49 in squares) # prints false

print("")
print("Iterating Through a Dictionary")

squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])

print("")
print("----------- End of dictionary -----------------")
