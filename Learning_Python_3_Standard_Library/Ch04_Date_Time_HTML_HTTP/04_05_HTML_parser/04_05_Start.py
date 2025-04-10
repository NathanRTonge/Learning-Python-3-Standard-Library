# HTML Parser Module
from html.parser import HTMLParser
"""HTML Review
<p> - open tag (paragraph)
</p> - close tag (paragraph)
<!-- notes --> - comment
<h1>Hello reader</h1> - an H1 header w/ data 'Hello reader'
"""

# First we create a class that inherits from HTMLParser to overwrite
#some methods
class HTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs): #self, tag, attributes
        """Prints the start tag and all attributes"""
        print("Start tag: ", tag)
        for attr in attrs:
            print("attr:", attr)
    def handle_endtag(self, tag):
        print("End tag: ", tag)
    def handle_comment(self, data):
        print("Comment: ", data)
    def handle_data(self, data): #what is inside each tag
        print("Data: ", data)


parser = HTMLParser()
parser.feed("<html><head><title>Coder</title></head><body><h1><!--hi-->I am a coder</h1></body></html>")
print() #this prints what was fed to the parser in the way we set out

#Try writing some html code in input eg:
#<h1>Hello, my name is Nathan.<!--this is a note--></h1><p>This is a paragraph!<!--this is a second note--></p>
input = input("Put in HTML Code")
parser.feed(input)
print()

#We can also analyse HTML from a file
htmlFile = open("sampleHTML.html", "r")
s = "" #empty string to be added to
for line in htmlFile:
    s += line
parser.feed(s)

print('\n')

htmlFile2 = open("sampleHTML2.html", "r")
b = ""
for line in htmlFile2:
    b += line
parser.feed(b)