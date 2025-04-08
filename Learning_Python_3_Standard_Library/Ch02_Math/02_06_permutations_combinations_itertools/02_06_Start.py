# Itertools Part 2
import itertools as it

# Permutations: Order matters - some copies with same inputs but in different order
election = {1: "Barb", 2:"Karen", 3:"Erin"}
for p in it.permutations(election):
    print(p)
print('\n')

for p1 in it.permutations(election.values()):
    print(p1)
print('\n')

# Combinations: Order does not matter - no copies with same inputs
colorsForPainting = ["Red", "Blue", "Purple", "Orange", "Yellow", "Pink"]
for c in it.combinations(colorsForPainting, 3): #3 is the number of values in each combination
    print(c)