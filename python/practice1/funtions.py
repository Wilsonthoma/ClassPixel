# A function is a block of code designed to perform a specific task.
# It is defined using the keyword def.

def calculate(a, b):
    return a + b

def greet():
    print("Hello Wilson")

greet()

# def     -> begins the function definition
# greet   -> the function name
# ()      -> holds any parameters
# :       -> begins the function body
# greet() -> calls the function


# Parameters and Arguments
# In the function below, "python" is the parameter
# and "to python course" is the argument.
# A function can accept multiple arguments, assigned to corresponding parameters.

def greet(python):
    print(f"Welcome {python}")

greet("to python course")


def student(name, age, school):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"School: {school}")

student("Wilson", 23, "Egerton University")


# The return statement
# The return keyword sends a value back to the calling code
# and ends the function execution.

def divide(a, b):
    return a / b

result = divide(10, 20)
print(result)


# A calculator using functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))
print("Division:", divide(a, b))