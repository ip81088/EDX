####-----VERTICAL-----####
# def main(): 
#     print_column(3)


# def print_column(hight):
#     for _ in range(hight):
#         print("#")

# def print_column(hight):
#     print("#\n" * hight, end="")
    
####--------HORIZONTAL--------####
# def main():
#     print_row(4)


# def print_row(width):
#     print("?" * width)


###-------SQUEARE--------###
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end=" ")
        print()



main()