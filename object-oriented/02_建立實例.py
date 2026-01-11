# 定義一個Person類別

from colorama import Fore, init

init(autoreset=True)


class Person:
    # 初始化方法
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


# 建立Person類別的物件
p1 = Person("張三", 18, "男")
p2 = Person("李四", 22, "女")

# 如果直接列印一個實例的話，我們是看不到實例身上的屬性的
print(p1)
print(p2)

# 透過點語法可以存取或修改實例身上的屬性
print(f"{Fore.GREEN}=== 存取或修改實例身上的屬性 ===")
print(p1.name)
print(p1.age)
print(p1.gender)
print("-" * 20)
print(p2.name)
print(p2.age)
print(p2.gender)
p1.name = "阿三"
print(p1.name)

# 透過 實例.__dict__ 可以查看實例身上的所有屬性
print(f"{Fore.GREEN}=== 透過 實例.__dict__ 可以查看實例身上的所有屬性 ===")
print(p1.__dict__)
print(p2.__dict__)

# 實例創建後，依然可以透過 實例.屬性名 = 值給實例追加屬性
print(f"{Fore.GREEN}=== 追加屬性 ===")
p1.address = "台北市中山區"
print(p1.__dict__)

# 透過type函式，可以查看某個實例物件，是由哪個類別建立出來的
print(type(p1))
print(type(p2))
