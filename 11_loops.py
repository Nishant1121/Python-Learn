"""
TOPIC: Loops
------------
for -> iterate over a known sequence (list, string, range, etc.)
while -> repeat until a condition becomes False
"""

# 1. for loop over a range
for i in range(5):          # 0,1,2,3,4 -> stop is EXCLUDED
    print(i)

for i in range(2, 10, 2):   # start, stop, step -> 2,4,6,8
    print(i)

# 2. for loop over a collection directly
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# 3. enumerate -> when you need both index AND value
for index, fruit in enumerate(fruits):
    print(index, fruit)

# 4. zip -> loop over two lists together, pairwise
names = ["Nishant", "Aman"]
scores = [85, 90]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# 5. while loop
count = 0
while count < 5:
    print("count is", count)
    count += 1

# 6. break -> exit loop immediately
for i in range(10):
    if i == 5:
        break
    print(i)

# 7. continue -> skip rest of this iteration, go to next
for i in range(5):
    if i == 2:
        continue
    print(i)

# 8. pass -> placeholder that does nothing (useful while writing code)
for i in range(3):
    pass   # TODO: implement later, won't error out meanwhile

# 9. else clause on loops -> runs ONLY if the loop completed WITHOUT break
for i in range(5):
    if i == 10:
        break
else:
    print("Loop finished without breaking")   # this runs

# 10. Nested loops -> classic pattern printing
for i in range(3):
    for j in range(3):
        print(f"({i},{j})", end=" ")
    print()



