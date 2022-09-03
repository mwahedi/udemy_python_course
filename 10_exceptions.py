print("######### EXCEPTION HANDLING")

## here we catch every exception that might occur
try:
    a = 5/0
except Exception as e:
    print(e)

## here we specify that we only want integers as input, if there's a differen value that throws an error
try:
    n = int(input("Enter an Integer: "))
except ValueError:
    print("That is not an Integer")

## here multiple things can go wrong, either dividing by zero or the file does not exist.
try:
    sum = 0
    file = open('numbers.txt', 'r')
    for number in file:
        sum = sum + 1.0/int(number)
    print(sum)
except ZeroDivisionError:
    print("Number in file is equal to zero.")
except IOError:
    print("File DNE.")
finally:
    print(sum)
    ## will throw an error, but close a file nonetheless.
    #file.close()

### RAISE
print("######### RAISE EXCEPTION")

a = 1

def RaiseException(a):
    if type(a) != type('a'):
        raise ValueError("This is not a string.")
    
try:
    RaiseException(a)
except ValueError as e:
    print(e)

def TestCase(a, b):
    assert a < b, "a is greater than b"

try:
        TestCase(2, 1)
except AssertionError as e:
    print(e)

