from colorama import Fore, init

init(autoreset=True)  

# 定義一個Person類別
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# 定義一個Student類別，繼承自Person類別
class Student(Person):
    def __init__(self, name, age, gender, stu_id, grade):
        super().__init__(name, age, gender)
        self.stu_id = stu_id
        self.grade = grade

p1 = Person('張三', 18, '男')
s1 = Student('李華', 12, '男', '2025001', '初二')

# 方法1：isinstance(instance, Class)，作用：判斷某個物件是否為指定類別或其子類別的實例
print(Fore.YELLOW + "s1 是 Student 的實例嗎？", isinstance(s1, Student))
print(Fore.YELLOW + "p1 是 Person 的實例嗎？", isinstance(p1, Person))
print(Fore.YELLOW + "s1 是 Person 的實例嗎？", isinstance(s1, Person))
print(Fore.YELLOW + "p1 是 Student 的實例嗎？", isinstance(p1, Student))

# 方法2：issubclass(Class1, Class2)，作用：判斷某個類別是否是另一個類別的子類別
print(Fore.BLUE + "Student 是 Person 的子類別嗎？", issubclass(Student, Person))
print(Fore.BLUE + "Person 是 Student 的子類別嗎？", issubclass(Person, Student))