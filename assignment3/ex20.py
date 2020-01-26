#imports a feature into python
from sys import argv
#sets the variables for the code
script, input_file = argv
#defines what file will be printed and read
def print_all(f):
    print(f.read())
#defines what file witll be rewound
def rewind(f):
    f.seek(0)
#defines how a line will be printed
def print_a_line(line_count, f):
    print(line_count, f.readline())
#sets a variable
current_file = open(input_file)
#phrase
print("First let's print the whole file:\n")
#prints the current file
print_all(current_file)
#phrase
print("Now let's rewind, kind of like a tape.")
#rewinds current file
rewind(current_file)
#phrase
print("Let's print these three lines:")
#indicates current line and states what will be printed into each line
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
