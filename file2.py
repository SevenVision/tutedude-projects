# Task: Write and Append Data to a File

# Step 1: Write user input to the file
user_text = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:   # 'w' overwrites the file
    file.write(user_text + "\n")

# Step 2: Append additional data to the same file
extra_text = input("Enter additional text to append: ")
with open("output.txt", "a") as file:   # 'a' adds to the file
    file.write(extra_text + "\n")

# Step 3: Read and display the final content of the file
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:   # 'r' reads the file
    for line in file:
        print(line.strip())
