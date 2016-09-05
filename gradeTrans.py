import sys

# Confirmation for the data entered
print("You have entered the grade: ")
print(sys.argv)

# Converts the data entered into a floating-point number
grade = float(sys.argv[1])

# Determining the letter grade of the number entered by using if and elif testing
if 97 <= grade <= 100:
    print("A+")
elif 93 <= grade <= 96:
    print("A")
elif 90 <= grade <= 92:
    print("A-")
elif 87 <= grade <= 89:
    print("B+")
elif 83 <= grade <= 86:
    print("B")
elif 80 <= grade <= 82:
    print("B-")
elif 77 <= grade <= 79:
    print("C+")
elif 73 <= grade <= 76:
    print("C")
elif 70 <= grade <= 72:
    print("C-")
elif 67 <= grade <= 69:
    print("D+")
elif 63 <= grade <= 66:
    print("D")
elif 60 <= grade <= 62:
    print("D-")
elif 0 <= grade <= 59:
    print("F")
elif grade < 0 or grade > 100:
    print("Error! Please enter a valid grade! (0~100)")
else:
    print("Error! Please enter a number!")
