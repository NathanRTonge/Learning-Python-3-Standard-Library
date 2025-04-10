# Text Wrap Module
# This module can help us format text
import textwrap

websiteText = """    Learning can happen anywhere with our apps on your computer,
mobile device, and TV, featuring enhanced navigation and faster streaming
for anytime learning. Limitless learning, limitless possibilities."""

print("No Dedent:")
#. fill(text) prints the text
print(textwrap.fill(websiteText), '\n')

print("Dedent")
#.dedent(text) removes the begining indent
dedent_text = textwrap.dedent(websiteText).strip()
print(dedent_text, '\n')

print("Fill")
#.fill(text, width=) fills to a certain width
print(textwrap.fill(dedent_text, width=50)) 
print(textwrap.fill(dedent_text, width=70), '\n')

print("Controlling Indent")
#sets the indent for the 1st and subsequent lines
print(textwrap.fill(dedent_text, initial_indent="   ", subsequent_indent="     "), '\n')

print("Shortening Text") 
#.sorten(text, width=, placeholder=) shortens the text to a certain
#length and replaces w/ a placeholder
short = textwrap.shorten("LinkedIn.com is great!", width=15, placeholder="...")
print(short)