# Random Module
import random as ran

# Random Numbers
print(ran.random()) #between 0-1
print(ran.randrange(10), '\n') #integer exclusive of 10 (0-9)

decider = ran.randrange(2) 
if decider == 0:
    print("HEADS", '\n')
else:
    print("TAILS", '\n')


print("You rolled a " + str(ran.randrange(1, 7)), '\n')

# Random Choices
# ran.sample(list, n) picks n objects from list
print(ran.sample(range(100), 5)) 
fruits =['apple', 'bannana', 'orange', 'kiwi', 'strawberry']
print(ran.sample(fruits,3), '\n')

#ran.choice(list) chooses one object from list at random
possiblePets = ["cat", "dog", "fish"]
print(ran.choice(possiblePets))
#ran.shuffle(list) randomises order of list
cards = ["Jack", "Queen", "King", "Ace"]
ran.shuffle(cards)
print(cards)