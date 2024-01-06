import random


def main():
    # Call get_level()
    level = get_level()
    # Get the score
    score = simulate_game(level)
    # print
    print("Score: ", score)


def get_level():
    # Loop forever
    while True:
    # Get level and check if it is between 1 and 3
        try:
            level = int(input("level: "))
            if level in [1,2,3]:
                break
        
        except:
            pass
    return level

def generate_integer(level):
    # Depending of the level, get a different random integer
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level ==2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x,y
# Simulate round (the math problem itself)
def simulate_round(x, y):
    tries = 1
    while tries <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                return True
            else:
                tries += 1
                print("EEE")
        
        except:
            tries += 1
            print("EEE")

    print(f"{x} + {y} = {x+y}")
    return False

# Simulate game
def simulate_game(level):
    round = 1
    score = 0
    while round <= 10:
        x, y = generate_integer(level)
        response = simulate_round(x,y)
        if response == True:
            score += 1
        round +=1
    return score



if __name__ == "__main__":
    main()