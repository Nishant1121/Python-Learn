"""
TOPIC: Lists
------------
Ordered, MUTABLE, allow duplicates. The most-used collection in Python.
Think of it like a JS array, but with more built-in methods.
"""

# 1. Creation & indexing
fruits = ["apple", "banana", "mango", "banana"]
print(fruits[0], fruits[-1])
print(fruits[1:3])          # slicing works same as strings

name = ["Nishant", "Sakshi", "Prashant"]
print(name[2],name[-2])
print(name[1:3])          # slicing works same as strings

# 2. Mutability -> unlike strings, this works fine
fruits[0] = "grape"
print(fruits)

# 3. Common methods
fruits.append("kiwi")           # add to end
fruits.insert(1, "orange")      # add at specific index
fruits.remove("banana")         # removes FIRST matching value
popped = fruits.pop()           # removes & returns last item
fruits.pop(0)                   # removes item at index 0
print(fruits, "| popped:", popped)

numbers = [5, 3, 8, 1, 9]
numbers.sort()                  # sorts in place, mutates original
print(numbers)
numbers.sort(reverse=True)
print(numbers)
numbers.reverse()
print(numbers)
# 4. extend vs append (common confusion)
a = [1, 2]
b = [3, 4]
a.append(b)      # -> [1, 2, [3, 4]]  adds b AS ONE element
c = [1, 2]
c.extend(b)      # -> [1, 2, 3, 4]    adds b's elements individually
print(a)
print(c)

# 5. Useful built-ins
print(len(numbers), max(numbers), min(numbers), sum(numbers))
print(3 in numbers)

# 6. List comprehension -> compact way to build lists
squares = [x ** 2 for x in range(1, 6)]
print(squares)
evens = [x for x in range(1, 20) if x % 2 == 0]
print(evens)

# 7. Nested lists (2D)
matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix[1][2])   # row 1, col 2 -> 6

# 8. Copying -> important gotcha
original = [1, 2, 3]
alias = original          # NOT a copy, points to same list
real_copy = original.copy()   # actual independent copy
alias.append(4)
print(original)           # also changed! -> [1, 2, 3, 4]
print(real_copy)          # unaffected -> [1, 2, 3]
