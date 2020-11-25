print(0o24)
print(0x11)
print(5e1)

# arithmetic operations

number1 = 3
number2 = 4
number3 = -3
print('division 3/4:', number1 / number2)
print('floordiv 4//3:', number2 // number1)
print('remainder 4%3:', number2 % number1)
print('negative 3:', -number1)
print('zero:', number1 + number3)
print('3 to the power of 4', number1 ** number2)

a = 3
b = 4
c = 5

result = (-b + pow((b ** 2) - 4 * a * c, 1 / 2)) / (2 * a)
print(result)

number4 = 0.75

print('type of number 0.75', type(number4))
print('type of result', type(result))

number5 = 1.0+2.3j
print('type of number 5', type(number5))

# string:

string1 = 'hello World'
string1 = """Hello World"""
string1 = u'Hello\nWorld'
print(string1)
string1 = r'Hello\nWorld'
print(string1)
string1 = f'Hello World: {string1}'
print(string1)

# string slices

result = string1[4]
print('foth char is :', result)
result = string1[-3]
print('third char is :', result)
result = string1[4:7]
print('seventh char is :', result)
result = string1[4:9:2]
print('ninth char is :', result)
result = string1[9:4:-1]
print('ninth char is :', result)
result = string1[-2:-7:-2]
print(' here it is:', result)

# dot notation for strings:
print('string actions:', dir(string1))
print(string1.lower())
print(string1.upper())
string1 = string1 + '{} {}'
print(string1.format(5,'abcd'))
print(string1.center(60 ," "))

print(number1.__add__(number2))
print((3).__add__(4))
print(number1.__mul__(number2))
print('division:', number1.__truediv__(number2))
print('power ok:', number1.__pow__(number2))