from colorama import Fore, init

init(autoreset=True)  

# 定義一個Person類別
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self, msg):
        print(Fore.GREEN + 'Person 類別', f'我叫{self.name}， 年齡是{self.age}， 性別是{self.gender}，我想說：{msg}')


# 定義一個Student類別，繼承自Person類別
class Student(Person):
    def __init__(self, name, age, gender, stu_id, grade):
        super().__init__(name, age, gender)
        self.stu_id = stu_id
        self.grade = grade

    # 方法重寫：當子類別中定義了一個與父類別中相同的方法，那麼子類別中的方法就會「覆蓋」父類別的方法
    def speak(self, msg):
        super().speak(msg)
        print(Fore.YELLOW + 'Student 類別', f'我是學生，我的學號是{self.stu_id}，我正在讀{self.grade}，我想說：{msg}')

s1 = Student('李華', 16, '男', '2025001', '高一')
s1.speak('好好學習')
