# Zipfile Module
import zipfile

# Open and List
zip = zipfile.ZipFile('Archive.zip', 'r')
# .namelist() lists the names of all files in zip folder
print(zip.namelist(), '\n')

# Metadata in the zip folder
# .infolist gives list of the metadata of the folder
for meta in zip.infolist():
    print(meta,)
print('\n')

# .getinfo(file) gets meta data for just that file
info = zip.getinfo("purchased.txt")
print(info, '\n')

# Access to files in zip folder
print(zip.read("wishlist.txt"))
# Or open the file to have more options with what to do w/ it
with zip.open('purchased.txt') as f:
    print(f.read())

# Extracting files
# To extract just on file: .extract(filename)
zip.extract("purchased.txt")
# To extract everything in the file: .extractall()
zip.extractall()

# Closing the zip
zip.close()