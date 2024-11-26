#!python3
"""
Debug this program so that it runs correctly

original code
x = 3
y = 7
z = 9

if x < y > z:
    print("the middle number is ", y)
else:
    print("the middle number is not",y)
"""

x=input("Enter a number:")
x=float(x)
y=input("Enter another number:")
y=float(y)
z=input("Enter another number:")
z=float(z)


if x < y < z:
    print("the middle number is ", y)
else:
    print("the middle number is not",y)