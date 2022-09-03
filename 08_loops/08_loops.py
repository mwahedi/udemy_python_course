### FOR LOOPS IN PYTHON

'''

for i in range(0,11):
    print(i)

## above statement is equal to for(int i=0, i<10, i++)

string = "String traversal!"
## can be achieved using indexes
for i in range(len(string)):
    print(string[i])

## or the actual characters
for char in string:
    print(char)

## nested for loops
for i in range(3):
    for j in range(2):
        print(j)

'''

## 10 x 10 multiplication table
for i in range(1,11):
    ## end="" helps us to remove the \n and have everything in one line
    print('{:<3}|'.format(i), end="")

    for j in range(1,11):
        print('{:>4}'.format(i * j), end="")
    
    if i == 1:
        print('\n{:#^44}'.format(""), end="") # prints a line of # below the first i
    print("")

### WHILE LOOPS
### Don't forget break and continue

