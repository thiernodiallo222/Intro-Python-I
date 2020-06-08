"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
print("%d" %x)
# y, and z:
print("%d %s %3.2f"%(x, 'and', y))
# x is 10, y is 2.25, z is "I like turtles!"
print('%s %d%s %s %3.2f%s %s "%s"' %('x is ', x,',',  'y is ', y,',',  'z is ', z))

# Use the 'format' string method to print the same thing
print("{0:2d}".format(x))

print("{0:2d}, and {1:3.2f}".format(x, y))

print('x is {0:2d}, y is {1:3.2f}, z is "{2}"'.format(x, y, z))

# Finally, print the same thing using an f-string
# print here
print(f'{x}')

print(f'{x} and {y}')

print(f'x is {x}, y is {y}, z is {z}')
