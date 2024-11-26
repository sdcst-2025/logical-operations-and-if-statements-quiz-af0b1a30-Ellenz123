"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
x=input("Enter a number:")
x=float(x)
y=input("Enter another number:")
y=float(y)

hypotenuse=input("is one of the numbers the hypotenuse of a right triangle? Yes or No")
if hypotenuse=="Yes":
   hypotenuse=max(x,y)
   side=min(x,y) 
   missingside=(hypotenuse**2+side**2)**0.5
else:
   missingside=(x**2+y**2)**0.5
missingside=round(missingside,1)
print(f"The length of missing side is {missingside}")