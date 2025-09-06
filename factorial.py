# Function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Input from user
num = int(input("Enter a number: "))

print(f"The factorial of {num} is: {factorial(num)}")
