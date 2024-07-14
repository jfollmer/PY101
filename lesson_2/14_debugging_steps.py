def process_student(student_data):
    name = student_data.get('name')
    grade = student_data.get('grade')
    return (name, grade)

def average_grade(grades):
    # print(grades)                 # testing to debug
    total = sum(grades)
    average = total / len(grades)
    return average

students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob'}, 
    {'name': 'Jack', 'grade': 72},
    {'name': 'Jane', 'grade': 75},
]
# testing to debug:
# students = {'name': 'Alice', 'grade': 85}
# students = {'name': 'Bob'}
# students = {'name': 'Alice', 'grade': 85}, {'name': 'Bob'}

def collect_grades(students):
    grades = []
    for student in students:
        name, grade = process_student(student)
        # grades.append(grade)      # old code
        # new code to fix error:
        if grade:
            grades.append(grade)
    return grades

grades = collect_grades(students)
print(average_grade(grades))

# new code to fix error, ultimately not used:
# try:                                
#     print(average_grade(grades))
# except Exception:
#     print("Something went wrong") 