
'''t1="Alice [85,90,78,92] bob [60,65,70,75] charlie [40,45,50,55]".split(" ")
tot=0
d={}
print(t1)
for i in range(len(t1)):
    for j in range(len(t1[i])):
                   if t1[i] != int():
                       tot += t1[i]
                   avg=tot/4
print(avg)'''
def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0

def highest_average_student(students_grades):
    highest_avg = -1
    top_student = ""
    
    for student, grades in students_grades.items():
        avg = calculate_average(grades)
        if avg > highest_avg:
            highest_avg = avg
            top_student = student
    
    return top_student

def count_students_passing(students_grades):
    passing_count = 0
    
    for grades in students_grades.values():
        if calculate_average(grades) >= 50:
            passing_count += 1
    
    return passing_count

def student_grades_tracker(students):
    # Create a dictionary from the input list of tuples (student_name, list_of_grades)
    students_grades = {student: grades for student, grades in students}
    
    # Output the dictionary of students and their grades
    print("Dictionary of students and their grades:")
    print(students_grades)
    
    # Example: Find the average grade for Bob
    student_name = "Bob"
    if student_name in students_grades:
        avg_grade = calculate_average(students_grades[student_name])
        print(f"\nAverage grade for {student_name}:")
        print(avg_grade)
    
    # Find the student with the highest average grade
    top_student = highest_average_student(students_grades)
    print(f"\nStudent with the highest average grade:")
    print(top_student)
    
    # Count the number of students who passed
    passing_students = count_students_passing(students_grades)
    print(f"\nNumber of students who passed:")
    print(passing_students)

# Example input
students = [
    ("Alice", [85, 90, 78, 92]),
    ("Bob", [60, 65, 70, 75]),
    ("Charlie", [40, 45, 50, 55]),
    ("David", [95, 100, 98, 92])
]

student_grades_tracker(students)


    
