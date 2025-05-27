import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

# The number of iterations is taken from the second argument.
# (Remember that in an array [0] is the first one, [1] is the second one.)
number_iterations = sys.argv[1]

f = open("output2.txt", "w")

for i in range(int(number_iterations)):
    if i < 5:
        f.write("The following number is less than 5\n")
    else:
        f.write("The following number is greater than or equal to 5\n")
    f.write(str(i)+"\n")

f.close()
print("look inside your folder...")