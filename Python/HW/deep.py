answer = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ')
answer = answer.title()

if answer == '42':
    print ('Yes')
elif answer == 'Forty-Two':
    print('Yes')
elif answer == 'Forty Two':
    print('Yes')
else:
    print('No')