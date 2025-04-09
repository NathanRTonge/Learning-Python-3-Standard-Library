# Iterative Files
myFile = open("scores.txt", "r")

# Read one line at a time with .readline()
print("My one line: " + myFile.readline())
myFile.seek(0)

# Iterate through each line of a file
# line.replace(before, after) replaces each before with after within
# the script but not in the original file
for line in myFile:
    newHighScorer = line.replace("BBB", "PDJ")
    print(newHighScorer)

myFile.close()