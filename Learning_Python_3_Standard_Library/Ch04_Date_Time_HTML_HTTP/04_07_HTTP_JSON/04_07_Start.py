# HTTP Package

theWebLink = 'https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224'

import urllib.request
import json
import textwrap

# This will print all of the text within the webpage
#(after decoding to utf-8)
with urllib.request.urlopen(theWebLink) as f:
    text = f.read()
    decodedtext = text.decode('utf-8')
    print(textwrap.fill(decodedtext, width=50))

print()

obj = json.loads(decodedtext)
print(obj['kind'], '\n')

print(obj['items'][0]['volumeInfo']['title'], ':')
print(obj['items'][0]['searchInfo']['textSnippet'])