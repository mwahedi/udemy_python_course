### OBJECT ORIENTED PROGRAMMING
print("######## OBJECT ORIENTED PROGRAMMING")

# when talking about OOP there are 4 concepts that are important
# hiding info: a user doesn't need to see implementations of the class instances to be able to use the class
# encapsulation: all variables (instances and methods) are grouped together, think: trucks, cars belong to the group vehicles
# inheritance: classes can be subclasses of other classes and take over some of the common methods / variables, e.g. all vehicles have 4 tires
# polymorphism: situations in which something occurs in several different forms, e.g. access objects of different types through the same interface

## CLASS DEFINITION
print("######## CLASS DEFINITION")

# class: a collection of attributes that are defined for any object
# data members, methods

class Complex:
    'This class simulates complex numbers.'
    def __init__(self, real = 0, imag = 0):
        'Standard constructor.'
        if(type(real) not in (int, float)) or type(imag) not in(int, float): 
            raise Exception('Arguments are not numbers!')
        self.real = real
        self.imag = imag

try: 
    c = Complex(2)
    print(c.real, c.imag)
    
    c = Complex((1,2,3),[1,2,3])
    print(c.real, c.imag)
except Exception as e:
    print(e)

## METHODS
print("######## METHODS")

class Complex:
    'This class simulates complex numbers.'
    def __init__(self, real = 0, imag = 0):
        'Standard constructor.'
        if(type(real) not in (int, float)) or type(imag) not in(int, float): 
            raise Exception('Arguments are not numbers!')
        self.real = real
        self.imag = imag

    ## getter methods
    def GetReal(self):
        return self.real
    
    def GetImag(self):
        return self.imag
    
    ## setter methods
    def SetReal(self, val):
        self.real = val
    
    def SetImag(self, val):
        self.imag = val

c = Complex(2.5, 5.2)
print(c.GetReal(), c.GetImag())
c.SetReal(5.2)
c.SetImag(2.5)
print(c.GetReal(), c.GetImag())

## can also initiate empty object of the class and use setters to set values

## METHODS PART 2
print("######## METHODS PART 2")

from inspect import getinnerframes
import math
class Complex:
    'This class simulates complex numbers.'
    def __init__(self, real = 0, imag = 0):
        'Standard constructor but now we\'re using private variables.'
        if(type(real) not in (int, float)) or type(imag) not in(int, float): 
            raise Exception('Arguments are not numbers!')
        self.__real = real
        self.__imag = imag

    ## getter methods
    def GetReal(self):
        return self.__real
    
    def GetImag(self):
        return self.__imag

    def GetModulus(self):
        'returns the modulus of the complex number'
        return math.sqrt(self.GetReal() * self.GetReal() + self.GetImag()*self.GetImag())

    def GetPhi(self):
        return math.atan2(self.GetImag(), self.GetReal())

    ## setter methods
    def SetReal(self, val):
        if type(val) not in (int, float):
            raise Exception('real part must be a number')
        self.__real = val
    
    def SetImag(self, val):
        if type(val) not in (int, float):
            raise Exception('imaginary part must be a number')
        self.__imag = val


c = Complex()

## we can't use the setters to interfere with the type of the objects private variables
try:
    c.SetReal((1,2,3))
except Exception as e:
    print(e)

## we can't just access the private variables of an object of the class anymore
try:
    print(c.__real)
except Exception as e:
    print(e)

c = Complex(-3, 4)
print(c.GetModulus(), c.GetPhi())

# we used methods within methods to calculate modulus & phi
# in the same vein we can also use methods to create the standard constructor
# e.g. self.SetReal(real) & self.SetImag(imag)


## METHODS PART 3
print("######## METHODS PART 3")
# Operator overloading

class Complex:
    'This class simulates complex numbers.'
    def __init__(self, real = 0, imag = 0):
        'Standard constructor but now we\'re using private variables.'
        if(type(real) not in (int, float)) or type(imag) not in(int, float): 
            raise Exception('Arguments are not numbers!')
        self.__real = real
        self.__imag = imag

    ## getter methods
    def GetReal(self):
        return self.__real
    
    def GetImag(self):
        return self.__imag

    def GetModulus(self):
        'returns the modulus of the complex number'
        return math.sqrt(self.GetReal() * self.GetReal() + self.GetImag()*self.GetImag())

    def GetPhi(self):
        return math.atan2(self.GetImag(), self.GetReal())

    ## setter methods
    def SetReal(self, val):
        if type(val) not in (int, float):
            raise Exception('real part must be a number')
        self.__real = val
    
    def SetImag(self, val):
        if type(val) not in (int, float):
            raise Exception('imaginary part must be a number')
        self.__imag = val

    ## operator overwriting is basically done here, we use the implementation of the __str__ methods
    ## that are part of pythons standard data model and overwrite them for the class
    def __str__(self) -> str:
        return str(self.GetReal()) + ' + ' + str(self.GetImag()) + 'i'

    ## operator overloading is done here, we basically add to the functionally of standard addition how
    ## complex addition is being done.
    def __add__(self, other) -> Complex:
        return Complex(self.GetReal() + other.GetReal(), self.GetImag() + other.GetImag())

    def __mul__(self, other):
        if type(other) in (int, float):
            return Complex(self.GetReal() * other, self.GetImag() * other)
        elif type(other) == Complex:
            return Complex(self.GetReal() * other.GetReal() - self.GetImag() * other.GetImag(),
            self.GetImag() * other.GetImag() + self.GetReal() * other.GetReal())
        raise Exception('Numbers must be real')

    def __truediv__(self, other):
        if type(other) in (int, float):
            if(other != 0):
                return Complex(self.GetReal() / float(other), self.GetImag() / float(other))
        elif type(other) == Complex:
            a, b, c, d = self.GetReal(), self.GetImag(), other.GetReal(), other.GetImag()
            nominator  = c * c + d * d
            if nominator != 0:
                return Complex((a*c + b*d) / nominator, (b*c - a*d) / nominator)
            else: 
                raise Exception('Nominator is zero.')

a = Complex(5, 0.3)
b = Complex(-3, 4)
print(a + b)
print(a * b)
print(a * 2)
print(a / b)
print(a / 2)


### CLASS INHERITANCE
print("######## CLASS INHERITANCE")

class Vehicle:
    def __init__(self, VIN, weight, manufacturer):
        self.vin_number = VIN
        self.weight = weight
        self.manufacturer = manufacturer
    
    def GetWeight(self):
        return self.weight
    
    def GetManufacturer(self):
        return self.manufacturer
    
    def VehicleType(self):
        pass

class Car(Vehicle):
    def __init__(self, VIN, weight, manufacturer, seats):
        ## instead of constructing every single variable like we do in the main class, we can use super() for the inheritance
        ## thus if the name of the class changes, we don't have to fiddle with the subclasses YAY
        super().__init__(VIN, weight, manufacturer)
        self.seats = seats

    def NumberOfSeats(self):
        return self.seats
    
    def VehicleType(self):
        return 'CAR'

class Truck(Vehicle):
    def __init__(self, VIN, weight, manufacturer, capacity):
        super().__init__(VIN, weight, manufacturer)
        self.capacity = capacity

    def TransportCapacity(self):
        return self.capacity
    
    def VehicleType(self):
        return 'TRUCK'

a = Car('ABC1', 1000, 'BMW', 4)
b = Truck('BCD2', 5000, 'MAN', 10000)
c = Car('DEF3', 1200, 'FORD', 4)
d = Truck('EFG4', 11000, 'MERCEDES', 15000)


print(a.GetWeight(), b.GetManufacturer(), c.NumberOfSeats(), d.TransportCapacity())
print("_____________________________________________________________________________________________")
print("Example of polymorphism, we are accessing multiple class objects through the same interface.")
for v in [a,b,c,d]:
    print(v.VehicleType() + " is of manufacturer: " + v.GetManufacturer())

### CLASS POSSIBLITIES IN PYTHON
print("######## CLASS POSSIBLITIES IN PYTHON")

# The complex class is going to inherit the Object class
class Complex(object):
    'This class simulates complex numbers.'
    def __init__(self, real = 0, imag = 0):
        'Standard constructor but now we\'re using private variables.'
        if(type(real) not in (int, float)) or type(imag) not in(int, float): 
            raise Exception('Arguments are not numbers!')
        self.__real = real
        self.__imag = imag

    ## getter methods
    def GetReal(self):
        return self.__real
    
    def GetImag(self):
        return self.__imag

    def GetModulus(self):
        'returns the modulus of the complex number'
        return math.sqrt(self.GetReal() * self.GetReal() + self.GetImag()*self.GetImag())

    def GetPhi(self):
        return math.atan2(self.GetImag(), self.GetReal())

    ## setter methods
    def SetReal(self, val):
        if type(val) not in (int, float):
            raise Exception('real part must be a number')
        self.__real = val
    
    def SetImag(self, val):
        if type(val) not in (int, float):
            raise Exception('imaginary part must be a number')
        self.__imag = val
    
    # we're going to work with properties, which are abstractions
    real = property(GetReal, SetReal)
    imag = property(GetImag, SetImag)

### SHARED VARIABLES
print("######## SHARED VARIABLES")
class Student(object):
    """Student"""
    number_of_students = 0

    def __init__(self, name, index):
        self.name = name
        self.index = index
        Student.number_of_students += 1 # every time there is a new student instantiated, increase the number of students.

s1 = Student('Python Pythonski', 12345)
s2 = Student('Guido van Rossum', 34567)
print(Student.number_of_students, s1.number_of_students, s2.number_of_students) # -> 2 2 2, they all share the same variable

# we can use destructors to remove students for example
del s1
print("Number of students was not updated, it's still: " + str(Student.number_of_students))

# we freed up the memory, but our shared variables needs to be updated
class Student(object):
    """Student"""
    number_of_students = 0

    def __init__(self, name, index):
        self.name = name
        self.index = index
        Student.number_of_students += 1 # every time there is a new student instantiated, increase the number of students.
    
    def __del__(self):
        Student.number_of_students -= 1

s1 = Student('Python Pythonski', 12345)
s2 = Student('Guido van Rossum', 34567)
del s1
print("Number of students was updated, it's now: " + str(Student.number_of_students))