# Least to Greatest
numbers = [0, -10, 15, -2, 1, 12]
sortedNumbers = sorted(numbers)
print(sortedNumbers, '\n')

# Alphabetically
# sorted() is case sensitive, capitals come before lowercase
children = ["Bob", "Bill", "Ben"]
print(sorted(children))
print(sorted(["Bob", "bill", "ben"]), '\n') 

# Key Parameters
# key= can be used to customise the sort order eg. making all values uppercase/case insensitive
print(sorted("My favorite child is Bob".split()))
print(sorted("My favorite child is Bob".split(), key=str.upper))
#reverse=True gives the list in descending order
print(sorted(numbers, reverse=True), '\n')

# For dictionaries, sorted will sort by the key
leaderBoard = {231: "CKL", 123:"ABC", 432:"JKC"}
print(sorted(leaderBoard, reverse=True), '\n')

students = [ ('Alice', 'B', 12), ('Eliza', 'A', 16), ('Tae', 'C', 15)]
# Can sort by different values within tuples by key=lambda num=num[i]
print(sorted(students, key=lambda student:student[0]))
print(sorted(students, key=lambda student:student[1]))
print(sorted(students, key=lambda student:student[2]))

