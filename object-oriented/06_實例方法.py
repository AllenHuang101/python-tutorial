# 定義一個Person類別
class Person:
    # 初始化方法（給實例新增屬性）
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 下面的speak方法、run方法，都保存在類別身上，但他們主要是供實例呼叫，所以他們都叫：實例方法
    # 自訂方法（給實例新增行為）
    def speak(self, msg):
        print(
            f"我叫{self.name}， 年齡是{self.age}， 性別是{self.gender}，我想說：{msg}"
        )

    # 自訂方法（給實例新增行為）
    def run(self, distance):
        print(f"{self.name}瘋狂的奔跑了{distance}公尺")


# 建立Person類別的實例物件
p1 = Person("張三", 18, "男")
p2 = Person("李四", 22, "女")

# print(Person.__dict__)
# print(p1.__dict__)
# print(p2.__dict__)

# 透過實例呼叫實例方法
p1.speak("你好")
p1.run(300)

# 透過類別去呼叫實例方法(能呼叫，但不推薦)
# Person.run(100) # 缺少實例參數會報錯
Person.run(p1, 100)  # 手動傳入實例參數
