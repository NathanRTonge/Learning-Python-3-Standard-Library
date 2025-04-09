# Tempfile Module
import tempfile

# Create a temporary file
tempFile = tempfile.TemporaryFile()

# Write to a temporary file
# .write takes a bytes object so a b'' is needed before the string
tempFile.write(b"Save this special number for me: 5009882300314")
tempFile.seek(0)

# Read the temporary file
print(tempFile.read())

# Close the temporary file (this deletes the file)
tempFile.close()