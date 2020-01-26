#From the system import a file
from sys import argv
#unpacks argument into two variables
script, filename = argv
#opens a file
txt = open(filename)
#prints a statement and what is in the file we chose
print(f"Here's your file {filename}:")
print(txt.read())
#prints the statement and then asks us to type the file again
print("Type the filename again:")
file_again = input ("> ")
#opens the same file as earlier
txt_again = open(file_again)
#prints text in the file
print(txt_again.read())

txt.close()
txt_again.close()
