# Get input from user
camelCase = input("camelCase: ")

# Print "snake_case"
print ("snake_case: ", end="")

# Loop through every letter
for letter in camelCase:

    # check if letter is upper case
    if letter.isupper():
        # print underscores and the letter in lowercase
        print("_" + letter.lower(), end="")
    # Otherwise print letter
    else:
        print(letter, end="")

# Print space in the end
print()