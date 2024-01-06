# Variable to keep track
amount_due = 50

# Loop until amount_due is greater than 0
while amount_due > 0:
    # Print the amount due
    print("Amount Due: ", amount_due)
    # Ask user to insert coin
    incert_coin = int(input("Incert Coin: "))
    # Check if coin is 25, 10 or 5 cents
    if incert_coin == 25 or 10 or 5:
        # Subtract value from amount_due
        amount_due -= incert_coin
       

# Calculate change_owed
change_owed = abs(amount_due)

# Print the result
print("Change Owed: ", change_owed)


# coke_price = int(50)

# while coke_price > 0:
#     amount_due = print("Amount Due: " + str(coke_price))
#     insert_coin = int(input("Insert Coin: "))

#     match insert_coin:
#         case 5|10|25:
#             coke_price = coke_price - insert_coin
#         case _:
#             coke_price = coke_price

# print("Change Owed: " + str(coke_price * -1))