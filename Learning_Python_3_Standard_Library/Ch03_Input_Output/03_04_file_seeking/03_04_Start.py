# Files and File Writing

# w --> write (replaces what is already in file)
# r --> read
# r+ --> read and write
# a --> append
# Open a file
myFile = open("scores.txt", "w")

# Show attributes and properties of that file
print("Name: " + myFile.name)
print("Mode: " + myFile.mode, '\n')

# Write to a file
myFile.write("GBJ : 100\nKHD : 99\nBBB : 89")
myFile.close()

# Read the file
myFile = open("scores.txt", "r")
print("Reading...: " + '\n' + myFile.read(19)) #10 is the characters to be read
myFile.seek(0)
print("Reading again: " + '\n' + myFile.read(19)) #seek pointer back at 0