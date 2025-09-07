import math

# Ask user for a number
num = float(input("Enter a number: "))

# Calculate using math module
square_root = math.sqrt(num)
natural_log = math.log(num)   # log base e
sine_value = math.sin(num)    # input is in radians

# Display results
print("\nResults:")
print(f"Square root of {num} = {square_root}")
print(f"Natural logarithm (base e) of {num} = {natural_log}")
print(f"Sine of {num} radians = {sine_value}")
