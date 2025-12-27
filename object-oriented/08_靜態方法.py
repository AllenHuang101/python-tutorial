from colorama import Fore, init
from datetime import datetime

init(autoreset=True)  

# 定義一個Person類別
class Person:
    # 初始化方法（給實例新增屬性）
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 靜態方法
    # 使用 @staticmethod 裝飾過的方法，就叫：靜態方法，靜態方法也是保存在類別身上的
    # 靜態方法只是單純的定義在類別中，它不會收到：self、cls參數，它收到的參數都是自訂參數
    # 由於靜態方法沒有收到：self、cls參數，所以其內部不會存取任何類別和實例相關的內容
    # 靜態方法通常用於定義：與「類別」相關的工具方法
    @staticmethod
    def is_adult(year):
        # 取得當前的年份
        current_year = datetime.now().year
        # 計算年齡
        age = current_year - year
        # 回傳結果（成年True，未成年False）
        return age >= 18

    @staticmethod
    def mask_idcard(idcard):
        return idcard[:3] + '********' + idcard[-3:]


# 驗證一下：靜態方法也是保存在類別身上的
print(Fore.YELLOW + "驗證1", Person.__dict__)

# 靜態方法需要透過類別去呼叫
result = Person.is_adult(2015)
print(Fore.YELLOW + "驗證2", result)
result2 = Person.mask_idcard('212101198802030028')
print(Fore.YELLOW + "驗證3", result2)

# 注意點：透過實例也能呼叫到靜態方法，但非常不推薦
p1 = Person('張三', 18, '男')
res = p1.mask_idcard('A126167889')
print(res)

