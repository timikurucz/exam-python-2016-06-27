# Create a function that takes a filename and a string as parameter,
# it should write the string to the file 3 times

# example: when called with "tree.txt" and "apple",
# it should write "appleappleapple" to the file "tree.txt".
# the function should not raise an error on any output problem, for example
# denied permission

def write_to_file(filename, string):
    try:
        f = open(filename, 'w')
        f.write(string * 3)
        f.close()
    except:
        pass

write_to_file('tree.txt', 'apple')
