answer = input('Expression: ')

x, y, z = answer.split(' ')

x = float(x)
z = float(z)

if y =='+':
    result = x + z
if y == '-':
    result = x - z
if y == '*':
    result = x * z
if y == '/':
    result = x / z

print(result)