## FILE MANAGEMENT
print("######### FILE MANAGEMENT")

# open(filename, access, buffering (optional))
file = open("file.txt")
print(file.read())
file.close()

## we can also read a specific amount of characters in a file
file = open("file.txt")
print(file.read(4))
file.close()

file = open("file.txt")
print(file.read(4))
## gives us the position of the pointer in the file
print(file.tell())
file.close()

file = open("file.txt")
print(file.read(4))
## seek goes to the position in the file
print(file.seek(5))
print(file.tell())
file.close()

## we can also read the file line by line
file = open("file2.txt")
for line in file:
    print(line)
file.close()

## we have different levels of access to the file's status
file = open("file2.txt")
print("File Name: " + file.name)
print("is closed: " + str(file.closed))
print("Mode " + file.mode)
file.close()

### WRITING TO A FILE
print("######### WRITING A FILE")
file = open("write.txt", "w+")
file.write("Hello file. I am string!")
## after writing a file, cursor is at the very end, we want it back to the beginning
file.seek(0)
print(file.read())
file.close()

## we can rewrite
file = open("write.txt", "w+")
file.write("Hello file. I am string!")
## after writing a file, cursor is at the very end, we want it back to the beginning
file.seek(0)
file.write("this")
file.seek(0)
print(file.read())
file.close()
