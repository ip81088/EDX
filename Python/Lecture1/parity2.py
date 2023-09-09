def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

# The best way
def is_even(n):
    return n % 2 = 0

# Much better way
# def is_even(n):
#     return True if n % 2 == 0 else False

# The not best way
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

main()