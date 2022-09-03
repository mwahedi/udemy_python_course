### FUNCTIONS

## decomposition breaks the code up in smaller chunks, making it easier to read
print("######### FUNCTIONS")
def function():
    print("This is our first function!")

function()

## Functions return values, which is another purpose besides decomposition

def returning():
    return "I am a result!"

# a good habit to assign the return value of a function to a variable
result = returning()
print(result)

def multival():
    return "this is a result", 2

print(multival())

### ARGUMENTS, PARAMETERS, SCOPE, NESTED
print("######### PARAMETERS")
def parameters(a):
    print(a)

parameters("This is a parameter!")

def add(a,b):
    c = a + b
    return c

result = add(12,5)
print(result)

# can also be done with strings
result = add("One", "word")
print(result)

## default parametrs
def default_param(a,b = 4,c = 5):
    return a + b + c

result = default_param(3)
print(result)

## SCOPE
print("######### SCOPE")
def scope(a):
    a = a + 1
    print(a)
    return(a)

scope(5)
#print(a) ## throws an error

def outer(a):
    def nested(b):
        return b * a
    a = nested(a)
    return(a)

print(outer(4))

## nested functions can be used to aggregate other functions

def f(a):
    def g(b):
        def h(c):
            return a * b * c
        return h
    return g
# we can call the nested function with multiple arguments
print(f(5)(2)(3))

### RECURSIVE FUNCTIONS
print("######### RECURSIVE FUNCTIONS")

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

## regular recursion
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)
## tail recursion
def tail_sum(n, accumulator = 0):
    if n == 0:
        return accumulator
    else:
        return tail_sum(n-1, accumulator+n)

print(sum(10))
print(tail_sum(10))

### LAMBDA FUNCTIONS
print("######### LAMBDA FUNCTIONS")
f = lambda x, y: x + y
print(f(2,3))

# example from before
f = lambda a: lambda b: lambda c: a * b * c
print(f(5)(3)(2))

# also works with nested functions and multiple arguments
f = lambda c: lambda a, b: lambda d: (c * (a + b)) % d
print(f(2)(4,3)(11))

