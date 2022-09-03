### REGULAR EXPRESSIONS

print("### REGULAR EXPRESSIONS")

# regex are being used to match expressions to strings and extract these from a big list of expressions

import re
from tokenize import group

print(re.search('pattern', 'Searching pattern in text'))
print(re.search('none', 'Searching pattern in text'))

match = re.search('pattern', 'Searching pattern in text')
print(match) #shows if match occurs and the span of the match (start, end)

print(match.re.pattern)
print(match.string)
print(match.start())
print(match.end())

# we can create a regex object that can be used for matching, using the compile function
print('### using the compile function')
regex = re.compile('pattern')
print(regex.search('Searching for patterns in text...').start())
print('### pattern occurs twice, use findall')
regex = re.compile('pattern')
print(regex.findall('Searching for patterns in text patterns...'))
print('### search for patterns occuring at the beginning of the string')
regex = re.compile('pattern')
print(re.match("Match", "Match function test"))
print(re.match("test", "Match function test."))

### CREATING PATTERNS

print("### CREATING PATTERNS")

def all_matches(text, pattern):
    print(pattern)
    regobj = re.compile(pattern)
    for m in regobj.finditer(text):
        print(str(m.start()) + '-' + str(m.end()) + ':' + text[m.start() : m.end()])

# * tells us: search for all x's that are followed by 0 or more y's.
# this is called greedy parsing
print("* tells us: search for all x's that are followed by 0 or more y's.")
all_matches('xyyxxxxxyyyyxxxxyy', 'xy*')
print("+ means find all matches where x is followed by 1 or more y's")
all_matches('xyyxxxxxyyyyxxxxyy', 'xy+') # + means find all matches where x is followed by 1 or more y's
print("? means find all matches where x is followed by 0 or 1 y")
all_matches('xyyxxxxxyyyyxxxxyy', 'xy?') # ? means find all matches where x is followed by 0 or 1 y
print("{2} means find those x that are followed by exactly the number  of y's specified")
all_matches('xyyxxxxxyyyyxxxxyy', 'xy{2}') # {2} means find those x that are followed by exactly the number  of y's specified
print("{3,4} means find those x that are followed by at least 3, but max 4 of y's specified")
all_matches('xyyxxxxxyyyyxxxxyy', 'xy{3,4}') # {3,4} means find those x that are followed by at least 3, but max 4 of y's specified
print("{2, } means find those x that are followed by at least 2 of y's specified")
all_matches('xyyxxxxxyyyyxxxxyy', 'xy{2,}') # {2, } means find those x that are followed by at least 2 of y's specified

# non-greedy parsing
print("non-greedy parsing")
all_matches('xyyxxxxxyyyyxxxxyy', 'xy*?')
all_matches('xyyxxxxxyyyyxxxxyy', 'xy+?')
all_matches('xyyxxxxxyyyyxxxxyy', 'xy{2}?')
all_matches('xyyxxxxxyyyyxxxxyy', 'xy??')

# matching with OR 
print("we can match using the or condition")
print("match all of the characters where x is followed by either x or y")
all_matches('xyyxxxxxyyyyxxxxyy', 'x[xy]+')

# matching without
print("we can match for characters that are 'the opposite' of what we define, using the NOT operator ^")
all_matches('xx.. ..yyyxxx.. ', '[^. ]+') # give me all characters that are followed by something, except whitespaces OR .

print("matching with range of ASCII letters")
all_matches('A94B2c5 xyz08', '[A-Z][0-9]')
all_matches('A94B2c5 xyz08', '[A-Za-z][0-9]')

print("matching with 'any character .'")
all_matches('Silk road', 'S.+k')

print("there are multiple other regex possibilities, e.g. \w, \D, etc")
all_matches("This is the 1-st example", r'\d+')
all_matches("This is the 1-st example", r'\D+')
all_matches("This is the 1-st example", r'\s+')
all_matches("This is the 1-st example", r'\S+')
all_matches("This is the 1-st example", r'\w+')
all_matches("This is the 1-st example", r'\W+')

print("Relative positioning in regular expressions")
all_matches('Relative positioning in regular expressions', r'^\w+') #find word at beginning of string
all_matches('Relative positioning in regular expressions', r'\A\w+') #find word at beginning of string
all_matches('Relative positioning in regular expressions', r'\w+$') #find word at end of string
all_matches('Relative positioning in regular expressions', r'\w+\Z') #find word at end of string
all_matches('Relative positioning in regular expressions', r'\br|w+$') #find letter r starting from the end of the string
all_matches('Relative positioning in regular expressions', r'\Bg\B') #find letter g in the middle of the string

### DIVISION AND GROUPING THE RESULTS
print("### DIVISION AND GROUPING THE RESULTS")
print("patterns can be divided into smaller groups and those then can be searched instead")

regex = re.compile('x([xy]+)(y)')
match = regex.search('xyxxxyxxxyxyxy')
print(match.groups())
print(match.group(1))
print(match.group(2))

print("we can give the groups names and then call the groups like that afterwards")
regex = re.compile('x(?P<first>[xy]+)(?P<second>y)')
match = regex.search('xyxxxyxxxyxyxy')
print(match.groups())
print(match.group('second'))
print(match.groupdict())

print("we can use the | operator for the OR")
regex = re.compile('y((x|y)+)')
match = regex.search('yxxyyxyxy')
print(match.group(1))
print(match.group(2))

### SETTING SEARCH PARAMETERS
print("### SETTING SEARCH PARAMETERS")

print("Flag ignore case")
print(re.findall('x*y', 'XXXYYYXXXY'), re.IGNORECASE)
print(re.findall('(^xy{2}) | (yx{2}$)', "xyxyxxxyxx\nxyyxxxxx"), re.MULTILINE)
print(re.findall('z.x', 'xyyyyz\nxyyxx'), re.DOTALL)

regex = re.compile('''
                            #This is comment
        \w+             #alphanumeric
    @               #at
    \w+             #alphanumeric
    .               #dot
    (com|net|org)   #com or org or net
''', re.VERBOSE)

print(regex.search('this@email12.com').start())

re.compile('pattern', re.IGNORECASE | re.VERBOSE | re.DOTALL)
print(re.findall('(?i)x*y', 'XXXYYYXXXy')) # ignore case