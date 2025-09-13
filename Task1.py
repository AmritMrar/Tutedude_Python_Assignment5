student_marks = { "Aman": 2, "Sham": 8, "Mohit": 9 , "Rana": 7, "Alice":85}
student_name= input("Enter the student name: ")
if student_name in student_marks :
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found.")