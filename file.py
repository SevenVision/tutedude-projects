# Task: Read a file and handle errors

try:
    # Try to open the file in read mode
    with open("sample.txt", "r") as file:
        # Read and print each line
        for line in file:
            print(line.strip())  # strip() removes extra spaces/newlines
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
except Exception as e:
    # Handle any other unexpected errors
    print("An error occurred:", e)
