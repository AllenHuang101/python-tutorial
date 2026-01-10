from colorama import Fore, init

init(autoreset=True)


# 1️⃣ 生成器：
#   1. 生成器函式：函式主體中如果出現了 yield 關鍵字，那該函式就是「生成器函式」。
#   2. 生成器物件：呼叫「生成器函式」時，其函式主體不會立刻執行，而是回傳一個「生成器物件」。
#   備註：不管能否執行到 yield 所在的位置，只要函式中有 yield 關鍵字，
#        那該函式就是「生成器函式」。
# region
def demo():
    print("demo 函式開始執行了")
    print(100)
    yield
    a = 200
    print(a)


print(f"{Fore.GREEN}生成器範例1")
d = demo()
print(d)
next(d)
# next(d)
# endregion


# 2️⃣ 寫在「生成器函式」中的程式碼，需要透過「生成器物件」來執行：
#   1. 呼叫「生成器物件」的 __next__ 方法，會讓「生成器函式」中的程式碼開始執行。
#   2. 當「生成器函式」中的程式碼開始執行後，遇到 yield 會「暫停」執行，
#      並且其內部會記錄「暫停」的位置。
#   3. 後續呼叫 __next__ 方法時，會從上一次「暫停」的位置繼續執行，
#      直到再次遇到 yield。
#   4. 遇到 return 會拋出 StopIteration 例外，
#      並將 return 後面的表達式作為例外資訊。
#   5. yield 後面所寫的表達式，會作為本次 __next__ 方法的回傳值。
# region
def demo2():
    print("demo 函式開始執行了")
    print(100)
    yield "我是第 1 個 yield 所回傳的資料"
    a = 200
    print(a)
    yield "我是第 2 個 yield 所回傳的資料"
    b = 300
    print(b)
    return "尚矽谷"


print(f"{Fore.GREEN}生成器範例2")
d = demo2()
# r1、r2 分別接收每次 yield 所回傳的資料
r1 = next(d)
print(r1)
r2 = next(d)
print(r2)
try:
    next(d)
except StopIteration as e:
    print(e)
# endregion


# 3️⃣ 生成器物件是一種特殊的迭代器
# （本質上是透過 yield 自動實作了迭代器協定）。
# region
def demo3():
    print("demo 函式開始執行了")
    print(100)
    yield "我是第 1 個 yield 所回傳的資料"
    a = 200
    print(a)
    yield "我是第 2 個 yield 所回傳的資料"
    b = 300
    print(b)
    return "尚矽谷"


print(f"{Fore.GREEN}生成器範例3")
d = demo3()
# 驗證：生成器物件 d，和迭代器一樣，也擁有 __iter__ 和 __next__ 方法
# print(hasattr(d, "__iter__"))
# print(hasattr(d, "__next__"))

# 驗證：生成器物件的 __iter__ 方法，
# 和迭代器一樣，回傳的也是自身
# result = iter(d)
# print(result == d)

# for 迴圈遍歷生成器
for index, item in enumerate(d):
    print(index, item)

# for 迴圈背後的邏輯
# gen = iter(d)
# while True:
#     try:
#         value = next(gen)
#         print(value)
#     except StopIteration:
#         break
# endregion


# 4️⃣ yield 也可以寫在迴圈中
print(f"{Fore.GREEN}生成器範例4")


# region
def create_car(total):
    for i in range(1, total + 1):
        yield f"我是第 {i} 台車"


# cars 是生成器物件
cars = create_car(5)

# 每呼叫一次 cars 的 __next__ 方法，就會得到一台車
c1 = next(cars)
print(c1)
c2 = next(cars)
print(c2)
c3 = next(cars)
print(c3)
c4 = next(cars)
print(c4)
c5 = next(cars)
print(c5)

# 生成器耗盡
# for car in cars:
#     print(car)
# endregion


# 5️⃣ yield from 可以把一個「可迭代物件」中的元素依序 yield 出來
# （可替代：for + yield）
# region
def demo4():
    nums = [10, 20, 30, 40]
    yield from nums


d = demo4()
r1 = next(d)
print(r1)
r2 = next(d)
print(r2)
r3 = next(d)
print(r3)
r4 = next(d)
print(r4)

for item in d:
    print(item)
# endregion

# 6️⃣ 使用：生成器.send(值)
# 可以在讓生成器繼續執行的同時，替上一次 yield 傳值
# 備註 1：next 只能取值，send 既能取值，也能送值
# 備註 2：第一次啟動生成器時，不能傳值！
# region
# def demo():
#     print("demo 函式開始執行了")
#     print(100)
#     a = yield "我是第 1 個 yield 所回傳的資料"
#     print(a)
#     b = yield "我是第 2 個 yield 所回傳的資料"
#     print(b)
#     return "尚矽谷"


# d = demo()
# r1 = d.send(None)
# print(r1)
# r2 = d.send(666)
# print(r2)
# try:
#     d.send(888)
# except StopIteration as e:
#     print(e)
# endregion

# 使用生成器實作遍歷 Person 類別的實例物件
# region
# class Person:
#     def __init__(self, name, age, gender, address):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.address = address
#         self.__attr = [name, age, gender, address]

#     def __iter__(self):
#         # yield self.name
#         # yield self.age
#         # yield self.gender
#         # yield self.address
#         yield from self.__attr


# p1 = Person("Bob", 18, "男", "台中")
# # 目標：
# for attr in p1:
#     print(attr)
# endregion


# 使用生成器實作斐波那契數列
# region
# def fibo(total):
#     pre = 1
#     cur = 1

#     for index in range(total):
#         if index < 2:
#             yield 1
#         else:
#             value = pre + cur
#             pre = cur
#             cur = value
#             yield value


# f1 = fibo(10)

# for item in f1:
#     print(item)

# 無論是迭代器還是生成器物件，
# 都可以用 list、tuple、set 等一次性取得其所有內容
# （注意：容易撐爆記憶體）
# result = set(f1)
# print(result)
# endregion

# 生成器表達式：
# 一種使用類似列表推導式語法，快速建立生成器物件的方式
# 語法格式：(表達式 for 變數 in 可迭代物件)
# 什麼時候適合使用生成器表達式？
# —— 當「每個結果只依賴當前這一個元素」時

# nums = [10, 20, 30, 40]

# 列表推導式
# result1 = [n * 2 for n in nums]
# print(result1)

# 生成器表達式
# result2 = (n * 2 for n in nums)
# for item in result2:
#     print(item)
