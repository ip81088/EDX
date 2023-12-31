# Create an empty dict
grocery = {}
# Loop forever
while True:
    try:
        # Get user input
        item = input().upper()
        # Check if item is already in the dict
        if item in grocery:
            # If it is, add 1 in the count
            grocery[item] += 1
        # Otherwise, add the item for the first time
        else:
            grocery[item] = 1
    except EOFError:
        # Print all the items in alphabetical order
        for key in sorted(grocery.keys()):
            print(grocery[key], key)
        # Stop the loop
        break