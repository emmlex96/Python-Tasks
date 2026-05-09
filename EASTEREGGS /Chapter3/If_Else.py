"""

INPUT grade
IF grade >= 90:PRINT "A"
ELIF grade >= 80:PRINT "B"
ELIF grade >= 70:PRINT "C"
ELIF grade >= 60:PRINT "D"
ELSE:PRINT "F"

"""

print("if...else Grade Classifier")
grade = int(input("Enter grade (0–100): "))

if grade >= 90:
    letter = 'A'
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade >= 60:
    letter = 'D'
else:
    letter = 'F'
    
print(f"Grade: {letter}")
