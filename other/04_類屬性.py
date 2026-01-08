class Student:
    student_count = 0


print(Student.__name__)
print(Student.student_count)
print(getattr(Student, "student_count"))
print(getattr(Student, "unknown", "10"))

Student.student_count = 89
setattr(Student, "student_count", 100)
print(Student.student_count)

Student.newattr = "new_value"
print(Student.newattr)


s1 = Student()
print(s1.student_count, Student.student_count, Student.__dict__)
s1.student_count = 50
print(s1.student_count, Student.student_count, Student.__dict__)
