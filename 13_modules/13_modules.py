## MODULES
print("###### MODULES")
## modules can be thought of as a way of program decomposition on the file level
## they enable us to re-use code

## we wrote a simple module that tests numbers if they are prime
## the folder level is important here: put the module where you can find it

'''
import prime as pr

pr.PrimesTo(100)

## instead of importing the whole module, we can import functions from the module with
## from prime import PrimesTo

## we also have functions for modules
## dir returns all the names of the functions that are defined in the module
print(dir(pr)

'''
## PACKAGES
print("###### PACKAGES")
## we can initiate a package by creating a file that starts with ___init__
## a package can include multiple modules

## we can import the package by using the . operator for navigating the folder structure
import main.sub2.prime as sub2 

sub2.PrimesTo(100)

## BUILT-IN MODULES
print("###### BUILT-IN MODULES")

## let's go back to the example of the shallow copy and try to make a deep copy

import copy

my_dict = {'Key': 'Values', ('K', 'E', 'Y'):5}
my_dict2 = copy.deepcopy(my_dict)

## now changing the original object doesn't change the other object
my_dict[1] = 1
print(my_dict)
print(my_dict2)

## another built-in module is math
import math as m

print(m.cos(m.pi))
print(m.exp(1))
print(m.ceil(1.6))

## complex math
import cmath as cm

print(dir(cm))
print(cm.sqrt(4))
print(cm.polar(complex(0,1)))

## random numbers
import random as ran

print(dir(ran))
print(ran.sample([1,2,3,4,5], 3))
print(ran.random())
print(ran.random())
## get random number from interval
print(ran.randint(5,100))

## sys gives information on constants and function that are 
## related to the python interpreter, e.g. path names
import sys

## max depth of recursion
print(sys.getrecursionlimit())
print(sys.version)
print(sys.path)
