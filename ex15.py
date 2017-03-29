from sys import argv

script, filename = argv

txt = open(filename)
#creates variable and then prints it into the console
#the variable stores the .txt name so it should in theory open any variable

#behind the scenes making a 'file object'
#


print "Here's your file %r:" % filename
print txt.read()


print"Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
