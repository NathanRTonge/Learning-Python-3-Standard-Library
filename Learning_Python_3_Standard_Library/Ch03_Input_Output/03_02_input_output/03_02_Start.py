# Output
print("Hello. This is an output (print)")

# Input
color = input("What is your favorite color? ")
print(color, '\n')

try:
    age = int(input('How old are you? '))
except Exception:
    print('Please input integer.')
    age = input('How old are you? ')
print(f'In 5 years you will be {int(age)+5} years old!')