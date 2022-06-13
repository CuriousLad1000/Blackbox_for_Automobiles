__author__ = 'shadowD'

#THIS IS MY INTRODUCTION TO PYTHON


a="hello"
print (a)

print('Hello')

# =========================================================================================================

b=3
c=199
d=b+c

print(d)


# =========================================================================================================

# READ TEXT FILE

v=open("H:\ssd2.txt",'r')
print v.read()

# =========================================================================================================

# WRITE TEXT FILE

W=open("H:\ssd3.txt",'w')  # use 'w' for overwriting previous file and 'a' to append at the end of file
W.write("hello world in the new file\n")
W.close()  #  When you are done with a file call F.close() to close it and free up
           # any system resources taken up by the open file.

# =========================================================================================================

# We can also specify how many characters the string should return, by using
# file.read(n), where "n" determines number of characters.

# This reads the first 5 characters of data and returns it as a string.

file = open('H:\ssd3.txt', 'r')
print file.read(5)


# =========================================================================================================


# file.readline( )

#  The readline() function will read from a file line by line (rather than pulling
#  the entire file in at once).

#  Use readline() when you want to get the first line of the file, subsequent calls
#  to readline() will return successive lines.

#  Basically, it will read a single line from the file and return a string
#  containing characters up to \n.

file2 = open('H:\ssd2.txt', 'r')
print file2.readline() # first line of file returned

# =========================================================================================================


file1 = open('H:\ssd2.txt', 'r')
print file1.readlines()          #  returns the complete ?le as a list of strings each separated by \n

# =========================================================================================================
## IMPORTANT

## For reading lines from a file, you can loop over the file object.
## This is memory efficient, fast, and leads to simple code.

file = open('H:\ssd2.txt', 'r')

for line in file:
    print line,  # NOTE ","   prevents the print from ending with a newline, allowing you to append
                 #  a new print to the end of the line.

# =====================================================================================================

# MULTI WRITE

fh = open("hello.txt", "w")
lines_of_text = ["a line of text", "another line of text", "a third line"]
fh.writelines(lines_of_text)
fh.close()

# =====================================================================================================

## With Statement

#  Another way of working with file objects is the With statement. It is good practice to use this statement.
# using the "With" statement, you get =====> better syntax and exceptions handling.
# In addition, it will =======>> automatically close the file. The with statement provides a
# way for ensuring that a clean-up is always used.

with open('H:\ssd4.txt') as file:  # Use file to refer to the file object
    data = file.read()
    print (data)

# ALT

with open("H:\ssd4.txt") as f:
    for shadowD in f:
        print shadowD,
# =====================================================================================================

# As a last example, we will show how to split lines from a text file.
# The split function in our example, splits the string contained in the variable data,
# whenever it sees a space character.
# You can split by whatever you wish, line.split(":") would split the line using colons.

with open('H:\ssd5.txt', 'r') as f:
    data = f.readlines()

    for line in data:
        words = line.split()
        print words