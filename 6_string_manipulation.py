string = 'I am a string in Python'
string1 = "I am a string in Python"

string[0]

len(string)

#inverse indexing (last character)
#immutable
print(string[-1]) #returns n
print(string[-2]) #returns o

print(string[5:11]) #slicing
print(string[:5])

# string concatenation
string2 = 2 * ('Con' + 'catenation')
print(string2)

# simple with variable
word = "Ford"
word = 'L' + word[1:]
print(word)

### Formatting

## how does format work
print("Today I had {0} cups of {1}".format(3, "coffee"))

print("prices: ({x}, {y}, {z})".format(x = 2.0, y= 1.5, z=5))
print("The {vehicle} had {0} crashes in {1} months".format(5, 6, vehicle = 'car'))

## string alignment

print("{:<20}".format("Text"))
print("{:>20}".format("Text"))

#format is useful for hexidecimal, binary, and octal values
print("{:b}".format(21))
print("{:x}".format(21))
print("{:o}".format(21))

### Specific characters

# use double quotes when there are single quotes in the string and vice versa
"I'm a string in python"
# or use escape characters
'I\'m a string in Python'

# backslashes can be used with r in front of the string
print(r'c:\number\nan')
# or triple quotations
print(""" \
    Hello:
            User defined look
            Python output
    """)