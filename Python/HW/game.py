import random

# Get level
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except:
        pass

# Set random number
rn = random.randint(1, level)

# Get the guess and check

while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < rn:
                print("Too small!")
            elif guess > rn:
                print("too large!")
            else:
                print("Just right!")
                break
    except:
        pass
