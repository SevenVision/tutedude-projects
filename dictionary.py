# Task: Create a Dictionary of Student Marks

# Step 1: Create a dictionary of students and their marks
student_marks = {
    "Ali": 85,
    "Zainab": 92,
    "Sara": 78,
    "Ahmed": 88,
    "Fatima": 95
}

# Step 2: Ask user to input a student's name
name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve marks or display message
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print(f"Sorry, {name} is not found in the record.")
