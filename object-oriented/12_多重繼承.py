from colorama import Fore, init

init(autoreset=True)  


# 概念：多重繼承指一個類別同時繼承多個父類別，從而擁有多個父類別的屬性和方法。
# 舉例：就像孩子不僅繼承爸爸的長相，也能繼承媽媽的性格。
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def speak(self):
        print(f'我叫{self.name}， 年齡是{self.age}， 性別是{self.gender}')

class Worker:
    def __init__(self, company):
        self.company = company
    def do_work(self):
        print(f'我在{self.company}工作')

class Student(Worker, Person):
    def __init__(self, name, age, gender, company, stu_id, grade):
        # 錯誤寫法，使用 super() 只能調用第一個父類別的初始化方法
        # super().__init(name, age, gender)
        # super().__init(company)
        Person.__init__(self, name, age, gender)
        Worker.__init__(self, company)
        self.stu_id = stu_id
        self.grade = grade
        
    def study(self):
        print(f'我在努力的學習，爭取做{self.grade}年級的第一名')

s1 = Student('張三', 18, '男', '麥當勞', '2025001', '高三')
print(Fore.YELLOW + "s1 的屬性：", s1.__dict__)

s1.speak()
s1.do_work()
s1.study()

# 類別的__mro__屬性：用於記錄屬性和方法的查找順序
# 透過實例去查找屬性或方法時，會先在自身實例上去查找，如果沒有，就按照__mro__記錄的順序去查找
print(Fore.BLUE + "Student 查找順序：", Student.__mro__)