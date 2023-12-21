# Get input from user
answer = input('Greeting: ')
answer = answer.title()

# All good no need to pay
if 'Hello' in answer:
    print('$0')
elif 'H' in answer[0]:
    print('$20')
else:
    print('$100')