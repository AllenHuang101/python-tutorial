from pprint import pprint
from colorama import Fore, init
from datetime import datetime


init(autoreset=True)


# 定義一個Person類別
class Person:
    # 類別屬性
    max_age = 120
    planet = "地球"

    # 初始化方法（給實例新增屬性）
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # speak方法、run方法，他們都屬於：實例方法
    def speak(self, msg):
        print(
            f"我叫{self.name}， 年齡是{self.age}， 性別是{self.gender}，我想說：{msg}"
        )

    def run(self, distance):
        print(f"{self.name}瘋狂的奔跑了{distance}公尺")

    # 使用 @classmethod 裝飾過的方法，就叫：類別方法，類別方法保存在類別身上的
    # 類別方法收到的參數：當前類別本身（cls）、自訂的參數
    # 因為收到了cls參數，所以類別方法中是可以存取類別屬性的
    # 類別方法通常用於實作與類別相關的邏輯，例如：操作類別級別的資訊、一些工廠方法
    @classmethod
    def change_planet(cls, value):
        cls.planet = value

    @classmethod
    def create(cls, info_str):
        # 從info_str中取得到有效資訊
        # 列表解包 (list unpacking)
        name, year, gender = info_str.split("-")
        # 取得當前年份
        current_year = datetime.now().year
        # 計算年齡
        age = current_year - int(year)
        # 創建並回傳一個Person類別的實例物件
        return cls(name, age, gender)


# 驗證一下：類別方法保存在類別身上的
print(Fore.YELLOW + "驗證一下：類別方法保存在類別身上的")
pprint(Person.__dict__)

# 類別方法需要透過類別調用
Person.change_planet("月球")
pprint(Person.__dict__)

# 建立Person實例
p1 = Person("張三", 18, "男")
p2 = Person("李四", 22, "女")

# 驗證一下：類別屬性planet已經修改了
print(Fore.YELLOW + "驗證一下：類別屬性planet已經修改了")
print(p1.planet)
print(p2.planet)

# 測試一下類別方法 —— create
print(Fore.YELLOW + "測試一下類別方法 —— create")
p3 = Person.create("李華-2003-女")
print(p3.__dict__)

# 注意點：類別方法，也能透過實例呼叫，但非常不推薦
print(Fore.YELLOW + "注意點：類別方法，也能透過實例呼叫，但非常不推薦")
p4 = p1.create("Jay-2003-男")
print(p4.__dict__)
