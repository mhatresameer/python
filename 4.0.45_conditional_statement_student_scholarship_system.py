"""
Student Scholarship System
Input:
Marks
Family Income
Rules:
Marks ≥ 90 and income < 3L → Full Scholarship
Marks ≥ 80 and income < 5L → Partial Scholarship
Otherwise → No Scholarship
"""

student_marks = int(input("Enter the marks you received: "))
student_family_income = float(input("Enter the family income: "))

if student_marks >= 90 and student_family_income < 300000:
  print("Full Internship.")
elif student_marks >= 80 and student_family_income < 500000:
  print("Partial Internship.")
else:
  print("No scholarship.")
