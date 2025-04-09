# Command Line Arguments
# in terminal, write:
# python [script path] "arg 1" "arg 2" etc.
import sys


# Print Arguments
# sys.argv gives a list of all cmd line arguments including the path/name of script
print("Number of arguments: ", len(sys.argv), ' arguments.')
print("Arguments ", sys.argv, '\n')

# Remove Arguments
sys.argv.remove(sys.argv[0])
print("Arguments", sys.argv, '\n')

# Sum up the Arguments
arguments = sys.argv
sum = 0
for arg in arguments:
    try:
        number = int(arg)
        sum = sum + number
    except Exception:
        print("Bad input")

print(sum)