## DATA STRUCTURES
print("###### DATA STRUCTURES")
print("###### TUPLES")

tup = (1, 'abc', 2, 'cde')
tup1 = 3, 'efg', True

tup2 = 'A' # is the same as tup2 = ('A', )
print(tup)
print(tup[1])
print(tup[0:2])

## contents of tuples are immutable objects, can't be changed after assignment

try:
    tup[3] = 5
except Exception as e:
    print(e)

## the tuple itself can be changed if need be
tup = tup[0:3] + (5, )
print(tup)
print(tup2 * 4)
print(5 in tup)

# we can also loop over tuples
for x in ('a', 'b', 'c'):
    print(x)

def multiple_result():
    return(1,2,'a')

print(multiple_result())

print((1,2,3) == (1,2))

### TUPLE FUNCTIONS
print("###### TUPLE FUNCTIONS")

tup = (2,5,1)
print(max(tup))
print(min(tup))

### LISTS
print("###### LISTS")

list1 = [1, 'abc', (2,3)]
## we can access the whole list, or elements in the list, with [][] we can access entries one level down
print(list1)
print(list1[2])
print(list1[2][0])
## we can duplicate
print(list1 * 2)
## we can check for membership
print(2 in list1)
## we can make comparisons
print(list1 == [1, 'abc', (2,3)])
## we can slice
print(list1[:2])
## we can add to the end of the list
list1.append(6)
print(list1)
list1[len(list1):] = [7]
print(list1)

### LIST FUNCTIONS
print("###### LIST FUNCTIONS")

## map function
## map takes a function and maps each value onto the function
print(list(map(lambda x: x**2 + 3*x + 1, [1,2,3,4])))

## filter
## returns every element in the list that is less than 4 as a list
print(list(filter(lambda x: x < 4, [1,2,3,4,5,4,3,2,1])))

## reduce
## reduce takes each value of the list and applies the function in sequence
## the example below baiscally does 1*2*3*4
## we need functools for reduce
import functools

print(functools.reduce(lambda x, y: x * y, [1,2,3,4]))


### DICTIONARIES
print("###### DICTIONARIES")

## dictionaries are collections of key : value pairs

my_dictionary = {'Key': 'Value', ('K', 'E', 'Y'): 5}
my_dictionary1 = {x: x+1 for x in range(10)}
## the order of the key value pairs is not kept as the print function will return the values as it finds them in the memory
print(my_dictionary)
print(my_dictionary1)
## we can find values by keys
print(my_dictionary['Key'])

try:
    print(my_dictionary[1])
except Exception as e:
    ## will print 1, which is not very informative, we want to understand that this is a key error
    print(e)

## we can access keys and values directly
print(my_dictionary.keys())
print(my_dictionary.values())

## we can add to the dictionary
my_dictionary1[1] = 2
print(my_dictionary1)

## we can delete
del my_dictionary1[1]
print(my_dictionary1)

## if you want to clear the dict
my_dictionary1.clear()
print(my_dictionary1)

### SHALLOW COPIES
print("###### SHALLOW COPIES")

## shallow copy means two copies of a data structure that share the same set of elements
my_dictionary = {'Item': 'Shirt', 'Size': 'Medium', 'Price': 50}
my_dictionary1 = my_dictionary

print(my_dictionary)
print(my_dictionary1)

## let's change an element

print(my_dictionary)
my_dictionary['Size'] = 'Small'
## we changed our first dictionary's entries, but also (because they access the same space in the memory)
## change the elements of the second dictionary.
## this can be unwanted, thus there are also deep copies.
print(my_dictionary1)

### SETS
print("###### SETS")

## sets are a collection of UNIQUE elements
## we can use union = |, intersection = ^ and difference = - 
## and more mathematical operations

my_set = set(['one', 'two', 'three', 'one'])
print(my_set)

my_set1 = set(['two', 'three', 'four'])
## union
print(my_set1 | my_set)
## difference
print(my_set1 - my_set)
## intersection
print(my_set1 ^ my_set)
## subset
a = my_set1 - my_set
print( a <= my_set)
print( a <= my_set1)
print( a >= my_set)
## we can add to sets
my_set.add('five')
print(my_set)

### SET FUNCTIONS
print("###### SET FUNCTIONS")

my_set = set(['one', 'two', 'three'])
my_set1 = set(['one', 'two', 'three', 'four'])

print(set.union(my_set, my_set1))
print(set.intersection(my_set, my_set1))
print(set.difference(my_set1, my_set))

