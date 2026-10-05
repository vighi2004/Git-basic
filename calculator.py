# Simple Calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = num1 + num2

print("Addition:", result)

subtract = num1 - num2
print("Subtraction:", subtract)

#lab 1b changes adding fucntionalies multplication and divide.
multiply = num1 * num2
print("Multiplication:", multiply)

if num2 != 0:
    divide = num1 / num2
    print("Division:", divide)
else:
    print("Cannot divide by zero")