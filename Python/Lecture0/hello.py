# Ask user for their name
name = input("What's your name? ")
# Can also be name = input("What's your name? ").strip().title() - and remove the next line with it

#Remove whitespace from str and capitalize user's name
name = name.strip().title()

#split user's name into first and last name
first, last = name.split()

# Say hello to the user
print(f"Hello, {name}")