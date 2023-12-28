# dict for fruits
fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe":50, 
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime":20,
    "nectarine": 50,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80,
}

# Get user input
x = input("Item: ")

# Loop through the dcit to find the fruit
for i in fruits:

    # Find the fruit asked (remember to user lowercase)
    if i in x.lower():
        
        # Print fruit calories
        print("Calories: ", fruits[i], end="")