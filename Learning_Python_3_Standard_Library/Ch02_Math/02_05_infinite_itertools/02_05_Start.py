# Itertools
# Tools for itarables
import itertools as it

# Infinite Counting
# it.count(start,step) starts from start and counts up in step infinitely
for x in it.count(50, 5): #start counting at 50 and go up in 5s
    print(x)
    if x == 80:
        break
print('\n')

# Infinite Cycling
# it.cycle(iterable) iterates over the iterable infinitely
x = 0
for c in it.cycle([1, 2, 3, 4]):
    print(c)
    x = x + 1
    if x > 23:
        break
x=0
for c in it.cycle('Racecar'):
    print(c)
    x = x + 1
    if x > 20:
        break
print('\n')

# Infinite Repeating
# it.repeat(value) infinitely repeats the value
for r in it.repeat(True):
    print(r)
    x = x + 1
    if x > 100:
        break;