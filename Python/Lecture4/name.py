import sys

# # The command needs to go in to the terminal $python name.py <NAME> and then hit ENTER
# print("Hello, my name is", sys.argv[1])

# try:
#     print("Hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")


# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("Hello, my name is", sys.argv[1])


# Gives you all the arguments that are after the filename
if len(sys.argv) < 2:
    print("Too few arguments")

for arg in sys.argv[1:]:
    print("Hello, my name is", arg)