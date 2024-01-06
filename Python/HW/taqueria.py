items = {
    
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Set current price to 0
price = 0

while True:
        try:
        # Get user input
            i = input("Item: ").title()
        # Check if item is already in the dict
            if i in items:
            # Add the item price to current price
                price += items[i]
            # Print current price
                print("Total: $", end="")
                print("{:.2f}".format(price))
        except EOFError:
        # Print a new line and stop the loop
            print()
            break