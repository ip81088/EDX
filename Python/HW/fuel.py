# While forever
while True:
    # Get user input
    fuel = input("Faraction: ")
    try:
        # Try to split the fuel
        x, y = fuel.split("/")
        # Convert into integers
        i = int(x)
        j = int(y)
        # Calculate the percentage
        f = i / j
        # Check if its less than 1 and stop the loop
        if f <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass
# Multiply percentage by 100
r = int(f * 100)
# Check if percentage is less than 1, print E
if r <= 1:
    print("E")
# check if percentage is greater than 99, print F
elif r >= 99:
    print("F")
# Otherwise print the %
else:
    print(f"{r}%")

# while True:
#     try:
#         tank_input = input("Fraction: ")
#         x, y = tank_input.split("/")
#         convert_x = int(x)
#         convert_y = int(y)
#         tank_percent = (convert_x / convert_y) * 100
#         if tank_percent <= 1:
#             print("E")
#             break
#         elif convert_x > convert_y:
#             pass
#         elif tank_percent >= 99:
#             print("F")
#             break
#         else:
#             print(round(tank_percent),"%", sep="")
#             break
#     except (ValueError, ZeroDivisionError):
#         pass