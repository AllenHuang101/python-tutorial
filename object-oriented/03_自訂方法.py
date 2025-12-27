# 定義一個Person類別
class Person:
    # 初始化方法（給實例新增屬性）
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 自訂方法（給實例新增行為）
    # speak方法收到的參數是：呼叫speak方法的實例物件（self）、其它參數
    # speak方法只有一份，保存在Person類別身上的，所有Person類別的物件，都可以呼叫到speak方法
    def speak(self, msg):
        print(f'我叫{self.name}， 年齡是{self.age}， 性別是{self.gender}，我想說：{msg}')

# 驗證一下：speak方法是存在Person類別身上的
print(Person.__dict__)

# 建立Person類別的實例物件
p1 = Person('張三', 18, '男')
p2 = Person('李四', 22, '女')

# 驗證一下：Person的實例物件身上是沒有speak方法的
print(p1.__dict__)
print(p2.__dict__)

# 所有Person類別的實例物件，都可以呼叫到speak方法
# 當執行p1.speak()的時候，查找speak方法的過程： 1.實例物件自身(p1)  =>  2.實例的「建造者」的身上(Person)
# p1.speak('好好學習')
# p2.speak('天天向上')

# 驗證一下上述的查找過程
def speak():
    print('巴拉巴拉巴拉巴拉巴拉')
    
p1.speak = speak
print("Person", Person.__dict__)
print("p1", p1.__dict__)
print("p2", p2.__dict__)
p1.speak()