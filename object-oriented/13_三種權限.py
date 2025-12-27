
from colorama import Fore, init

init(autoreset=True) 

class Person:
    def __init__(self, name, age, idcard):
        # 公有屬性：當前類別中、子類別中、類別外部，都可以存取
        self.name = name
        # 受保護的屬性：當前類別中、子類別中，都可以存取
        self._age = age
        # 私有屬性：僅能在當前類別中存取
        self.__idcard = idcard  
        
    def speak(self):
        print(Fore.YELLOW + '當前類別中可以存取「公有屬性」、「受保護的屬性」、「私有屬性」', f'我叫：{self.name}，年齡：{self._age}， 身份證：{self.__idcard}')

class Student(Person):
    def hello(self):
        print(Fore.GREEN + '子類別可以存取「公有屬性」、「受保護的屬性」', f'我是學生（{self.name}-{self._age}）')
        # print(Fore.RED + '子類別不能存取「私有屬性」', self.__idcard)  # 會報錯！

p1 = Person('張三', 18, 'A123123123')
# 當前類別中可以存取「公有屬性」、「受保護的屬性」、「私有屬性」
p1.speak()

s1 = Student('李四', 18, 'A123123123')
s1.hello()

# 在類別的外部，可以存取【公有屬性】
print(p1.name)

# 在類別的外部，如果強制存取【受保護的屬性】也能存取到，但十分不推薦！
print(p1._age)

# 在類別的外部，如果強制存取【私有屬性】不能存取到，而且會報錯！
# print(p1.__idcard)


# (重要!!!)Python底層是透過重新命名的方式，實現私有屬性的
print(p1.__dict__)
print(Fore.RED + "私有屬性是透過重新命名實現的：", p1._Person__idcard)