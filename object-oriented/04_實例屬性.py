# 定義一個Person類別
class Person:
    # 初始化方法
    def __init__(self, name, age, gender):
        # 透過【實例.屬性名 = 值】給實例新增的屬性，就叫實例屬性
        # 實例屬性只能透過實例存取，不能透過類別存取
        # 每個實例都有自己【獨一份的】實例屬性，各個實例之間是互不干擾的
        self.name = name
        self.age = age
        self.gender = gender


# 建立Person類別的實例物件
p1 = Person("張三", 18, "男")
p2 = Person("李四", 22, "女")

print(p1.name)

# 實例屬性只能透過實例存取，不能透過類別存取
# print(Person.name)
