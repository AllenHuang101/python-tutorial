from colorama import Fore, init

init(autoreset=True)  

# 定義一個Person類別
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self, msg):
        print(f'我叫{self.name}， 年齡是{self.age}， 性別是{self.gender}，我想說：{msg}')

# 定義一個Student類別（子類別、派生類別）， 繼承自Person類別（父類別、超類別、基類別）
class Student(Person):
    def __init__(self, name, age, gender, stu_id, grade):
        # 在子類別中，有兩種方式去呼叫父類別的初始化方法，來實現對繼承屬性：name, age, gender 初始化操作
        # 方式1（更推薦）
        super().__init__(name, age, gender)

        # 方式2，Self 要自己傳過去
        # Person.__init__(self, name, age, gender)

        # 子類別獨有的屬性，需要自己手動完成初始化
        self.stu_id = stu_id
        self.grade = grade

    def study(self):
        print(f'我叫{self.name}，我在努力的學習，爭取做到{self.grade}年級的第一名')

# 建立Student類別的實例物件
s1 = Student('李華', 16, '男', '2025001', '高一')
print(Fore.YELLOW + "驗證1", s1.__dict__)
print(type(s1))

# 查找speak方法的過程：1.實例自身(s1) => 2.Student類別 => 3.Person類別
s1.speak('你好')

# 查找study方法的過程：1.實例自身(s1) => 2.Student類別 => 3.Person類別
s1.study()


s1.speak = lambda msg: print('這是s1上的speak方法', f'我是{s1.name}，我想說：{msg}')
# 查找study方法的過程：1.實例自身(s1) => 2.Student類別 => 3.Person類別
s1.speak('大家好')