# Define the calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Python3 program to add two numbers with full sum output
#initialise variables to 0
num1 = 0.0
num2 = 0.0
result = 0.0

#get the variables from the command line
# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#get the operator type
operator = input("Enter operator (+,-,*,/): ")
# Adding two nos
# Perform calculation based on user input
if operator == "+":
    result = add(num1, num2)
elif operator == "-":
    result = subtract(num1, num2)
elif operator == "*":
    result = multiply(num1, num2)
elif operator == "/":
    result = divide(num1, num2)
else:
    result = "Error: Invalid operator"


# printing values
print("The result of {0} {3} {1} is {2}" .format(num1, num2, result, operator))
