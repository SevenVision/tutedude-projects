# Task: Demonstrate List Slicing

# Step 1: Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Step 2: Extract the first five elements
first_five = numbers[:5]   # from index 0 to 4

# Step 3: Reverse these extracted elements
reversed_list = first_five[::-1]

# Step 4: Print results
print("Original list:", numbers)
print("First five elements:", first_five)
print("Reversed list of first five elements:", reversed_list)
