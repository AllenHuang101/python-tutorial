# 迭代器是一次性的，狀態只會向前推進，且不會自動重置（迭代器在遍歷的過程中會被「消耗」）。
# region
# names = ['張三', '李四', '王五']
# it1 = iter(names)
# it2 = iter(names)

# print(it1)
# print(it2)

# print(next(it1))
# print(next(it1))
# print(next(it1))

# print(next(it2))
# print(next(it2))
# print(next(it2))

# for item in it1:
#     print(item)
#
# for item in it2:
#     print(item)
# endregion


# 需求：讓 for 迴圈可以遍歷 Person 的實例物件
# 實作方式1️⃣
# region
# class Person:
#     def __init__(self, name, age, gender, address):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.address = address

#     def __iter__(self):
#         return PersonIterator(self)


# class PersonIterator:
#     def __init__(self, p):
#         # 將外部傳進來的資料保存好
#         self.p = p
#         # 設定迭代器的初始化狀態（指標位置）
#         self.index = 0
#         # 配置好要遍歷的內容
#         self.attrs = [p.name, p.age, p.gender, p.address]

#     # 迭代器的 __iter__ 方法會回傳迭代器自身
#     def __iter__(self):
#         return self

#     # 每次呼叫 __next__ 方法，會依據目前的狀態，回傳下一個元素
#     def __next__(self):
#         # 如果指標的位置超出範圍，那就拋出 StopIteration 例外
#         if self.index >= len(self.attrs):
#             raise StopIteration
#         # 取得要回傳的內容
#         value = self.attrs[self.index]
#         # 更新迭代器狀態（指標位置）
#         self.index += 1
#         # 回傳 value
#         return value


# # 目標：
# p1 = Person("Bob", 38, "男", "台北市中正區")

# for item in p1:
#     print(item)

# for item in p1:
#     print(item)
# endregion


# 實作方式2️⃣
# region
# class Person:
#     def __init__(self, name, age, gender, address):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.address = address
#         # 設定迭代器的初始化狀態（指標位置）
#         self.__index = 0
#         # 配置好要遍歷的內容
#         self.__attrs = [name, age, gender, address]

#     def __iter__(self):
#         self.__index = 0
#         return self

#     def __next__(self):
#         # 如果指標的位置超出範圍，那就拋出 StopIteration 例外
#         if self.__index >= len(self.__attrs):
#             raise StopIteration
#         # 取得要回傳的內容
#         value = self.__attrs[self.__index]
#         # 更新迭代器狀態（指標位置）
#         self.__index += 1
#         # 回傳 value
#         return value


# # 目標：
# # 下面的 p1 既是可迭代物件，又是迭代器
# p1 = Person("Bob", 38, "男", "台北市中正區")

# for item in p1:
#     print(item)

# for item in p1:
#     print(item)
# endregion


# 進階：迭代器玩的就是 __next__
# from cn2an import an2cn


# class Person:
#     def __init__(self, name, age, gender, address):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.address = address
#         # 設定迭代器的初始化狀態（指標位置）
#         self.__index = 0
#         # 配置好要遍歷的內容
#         self.__attrs = [name, age, gender, address]

#     def __iter__(self):
#         self.__index = 0
#         return self

#     def __next__(self):
#         # 如果指標的位置超出範圍，那就拋出 StopIteration 例外
#         if self.__index >= len(self.__attrs):
#             raise StopIteration
#         # 取得要回傳的內容
#         value = self.__attrs[self.__index]
#         # 將字串轉為大寫
#         if isinstance(value, str):
#             value = value.upper()
#         # 將數字轉為漢語形式
#         if isinstance(value, int):
#             value = an2cn(value)
#         # 更新迭代器狀態（指標位置）
#         self.__index += 1
#         # 回傳 value
#         return value


# # 目標：
# # 下面的 p1 既是可迭代物件，又是迭代器
# p1 = Person("Bob", 18, "男", "新北市")

# for item in p1:
#     print(item)
