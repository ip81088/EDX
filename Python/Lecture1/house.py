name = input("What's your name? ")
# Makes sure that the name will start in capital letter so the rest of the code won't give worng messages
name = name.title()

match name:
    case "Harry":
        print("Gryffindor")
    case "Harmione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
# Every other name in the world
    case _:
        print("Who?")