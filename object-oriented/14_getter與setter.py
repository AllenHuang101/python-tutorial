from colorama import Fore, init

init(autoreset=True) 

class Person:
    max_age = 120

    def __init__(self, name, age, idcard):
        self.name = name        # 公有屬性：當前類別中、子類別中、類別外部，都可以存取
        self._age = age         # 受保護的屬性：當前類別中、子類別中，都可以存取
        self.__idcard = idcard  # 私有屬性：僅能在當前類別中存取

    # 註冊age屬性getter方法，當讀取Person實例的age屬性時，下面的age方法就會被自動呼叫
    @property
    def age(self):
        return self._age

    # 註冊age屬性setter方法，當修改Person實例的age屬性時，下面的age方法就會被自動呼叫
    @age.setter
    def age(self, value):
        if value <= Person.max_age:
            self._age = value
        else:
            print('年齡非法，修改失敗！')

    # 註冊idcard屬性getter方法，當存取Person實例的idcard屬性時，下面的idcard方法就會被自動呼叫
    @property
    def idcard(self):
        return self.__idcard[:3] + '********' + self.__idcard[-3:]

    # 註冊idcard屬性setter方法，當修改Person實例的idcard屬性時，下面的idcard方法就會被自動呼叫
    @idcard.setter
    def idcard(self, value):
        print(f'抱歉身份證號碼不允許修改，如有特殊需求，請聯繫管理員！, {value}')

p1 = Person('張三', 18, 'A123123123')
print(p1.name)
# 會有警告，但能正常執行
# print(p1._age)
print(Fore.YELLOW + "p1.age:",p1.age)

p1.age = 15
print(Fore.YELLOW + "p1.age:",p1.age)

print(Fore.YELLOW + "p1.idcard:",p1.idcard)
p1.idcard = 'B987654321'
