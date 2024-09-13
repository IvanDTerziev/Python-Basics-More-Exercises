total_grades = 0
top_students = 0
between_4_and_5 = 0
between_3_and_4 = 0
failed = 0

count_of_students = int(input())

for _ in range(count_of_students):
    student_grade = float(input())
    total_grades += student_grade
    if student_grade >= 5:
        top_students += 1
    elif student_grade >= 4:
        between_4_and_5 += 1
    elif student_grade >= 3:
        between_3_and_4 += 1
    else:
        failed += 1

print(f"Top students: {top_students / count_of_students:.2%}")
print(f"Between 4.00 and 4.99: {between_4_and_5 / count_of_students:.2%}")
print(f"Between 3.00 and 3.99: {between_3_and_4 / count_of_students:.2%}")
print(f"Fail: {failed / count_of_students:.2%}")
print(f"Average: {total_grades / count_of_students:.2f}")