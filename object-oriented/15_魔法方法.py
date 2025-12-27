# 概念：以 __xxx__ 命名的特殊方法（雙底線開頭和結尾）。
# 特點：不需要我們手動呼叫，我們只要準備好這些方法，Python會在特定場景下，去自動呼叫。

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 當執行print(Person的實例物件) 或 str(Person的實例物件) 時呼叫
    def __str__(self):
        return f'{self.name}-{self.age}-{self.gender}'

    # 當執行len(Person的實例物件) 時呼叫
    def __len__(self):
        return len(p1.__dict__)

    # 當執行 Person實例物件1 < Person實例物件2 時呼叫
    def __lt__(self, other):
        return self.age < other.age

    # 當執行 Person實例物件1 > Person實例物件2 時呼叫
    def __gt__(self, other):
        return self.age > other.age

    # 當執行 Person實例物件1 == Person實例物件2 時呼叫
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # 當存取Person實例身上不存在的屬性時呼叫
    def __getattr__(self, item):
        return f'您存取的{item}屬性不存在'

p1 = Person('張三', 21, '男')
p2 = Person('李四', 22, '男')
# 呼叫 __str__ 方法
print(p1)
print(p2)

# 呼叫 __len__ 方法
LEN = len(p1)
print(LEN)

# 呼叫 __lt__ 方法
print(p1 < p2)

# 呼叫 __gt__ 方法
print(p1 > p2)

# 呼叫 __eq__ 方法
print(p1 == p2)

# 呼叫 __getattr__ 方法
print(p1.address)
