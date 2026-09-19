# input score from user
score = int(input("Enter your score: "))
# determine grade based on score
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
# print the grade
print("Grade:", grade)
