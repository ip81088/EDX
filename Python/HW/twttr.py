# ask user for an input of string
answer = input("Input: ")
# print output
print("Output: ", end='')
# loop through every letter
for letter in answer:
    # check if it is not vowls wther inputted in upper or lower case
    if not letter.lower() in ['a', 'o', 'i', 'u', 'e']:
        # print the letter
        print(letter, end='')

# print new line
print()