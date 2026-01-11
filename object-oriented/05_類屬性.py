from pprint import pprint
from colorama import Fore, init

init(autoreset=True)


# 定義一個Person類別
class Person:
    # max_age、planet 都是類屬性，類屬性是保存在類別身上的
    # 類屬性可以透過類別訪問，也可以透過實例訪問
    # 類屬性通常用於保存：公共資料
    max_age = 120
    planet = "地球"

    # 初始化方法
    def __init__(self, name, age, gender):
        # 給實例新增屬性
        self.name = name
        self.gender = gender
        # 限制age的最大值
        if age <= Person.max_age:
            self.age = age
        else:
            print(f"年齡超出範圍了，已經將年齡設定為最大值：{Person.max_age}")
            self.age = Person.max_age


print(f"{Fore.GREEN}=== 驗證：類別屬性是保存在類別身上的 ===")

# 驗證一下：類別屬性是保存在類別身上的
pprint(Person.__dict__)

# 建立Person類別的實例物件
p1 = Person("張三", 18, "男")
p2 = Person("李四", 22, "女")

# 驗證一下：實例身上是沒有類別屬性的

print(f"{Fore.GREEN}=== 實例身上是沒有類別屬性的 ===")
print("p1", p1.__dict__)
print("p2", p2.__dict__)


# 驗證一下：類別屬性可以透過類別存取，也可以透過實例存取

print(f"{Fore.GREEN}=== 類別屬性可以透過類別存取，也可以透過實例存取 ===")
print(Person.max_age)
print(p1.max_age)  # 查找 max_age 的過程：1.實例自身(p1)  => 2.實例的「建造者」(Person)
print(p2.planet)
print("-" * 100)

print(f"{Fore.GREEN}=== 測試一下年齡超出範圍 ===")
p3 = Person("王五", 170, "女")
print(p3.__dict__)

print("-" * 100)

# 進行【實例.屬性名 = 值】操作時，只會對實例自身的屬性起作用，不會影響類別屬性
print(
    f"{Fore.GREEN}===  進行【實例.屬性名 = 值】操作時，只會對實例自身的屬性起作用，不會影響類別屬性 ==="
)
p1.planet = "火星"
print(Person.__dict__)
print(p1.__dict__)
print(p2.__dict__)
print(p1.planet)
print(p2.planet)
