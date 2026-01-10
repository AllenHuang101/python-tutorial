from typing import List
from colorama import Fore, init

init(autoreset=True)

# 定義有內容的列表
list1 = [34, 56, 21, 56, 11]
list2 = ["北京", "尚矽谷", "你好啊"]
list3 = [23, "尚矽谷", True, None]
list4 = [23, "尚矽谷", True, None, [100, 200, 300]]
# 定義空列表（列表中的資料，後面會透過特定寫法填充）
list5 = []
list6 = list()

print(list1, type(list1))
print(list2, type(list2))
print(list3, type(list3))
print(list4, type(list4))
print(list5, type(list5))
print(list6, type(list6))
