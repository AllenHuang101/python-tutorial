# 定義一個Person類別（類別名稱通常使用：大駝峰寫法）
class Person:
    # 說明：當一個函式被定義在了類別中時，那這個函式就被稱為：方法。
    # __init__方法：初始化方法，主要作用：給當前正在建立的實例物件新增屬性
    # __init__方法收到的參數：當前正在建立的實例物件（self）、其它的自訂參數
    # 當我們以後編寫程式碼去建立Person類別實例的時候，Python會自動呼叫__init__方法
    def __init__(self, name, age, gender):
        # 給實例新增屬性（語法為：self.屬性名 = 值）
        self.name = name
        self.age = age
        self.gender = gender