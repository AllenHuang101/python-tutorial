from colorama import Fore, init

init(autoreset=True)

# 列表推導式：用一條簡潔語句，從可迭代物件中，生成新列表的語法結構。
# 備註：列表推導式本質上是 for 迴圈 + append() 的一種簡寫形式。
# 語法格式：[表達式 for 變數 in 可迭代物件]

# 需求：讓列表中每個元素都變為原來的 2 倍，得到一個新的列表

# 方式一：用 map 函式
nums = [10, 20, 30, 40]
# map 函式會返回的是一個迭代器，需要用 list() 函式轉換為列表
result = list(map(lambda n: n * 2, nums))
print(f"{Fore.GREEN}方式一：用 map 函式", result)

# 方式二：用 for 迴圈 + append()
nums = [10, 20, 30, 40]
result = []
for n in nums:
    result.append(n * 2)
print(f"{Fore.GREEN}方式二：用 for 迴圈 + append()", result)

# 方式三：用列表推導式
nums = [10, 20, 30, 40]
result = [n * 2 for n in nums]
print(f"{Fore.GREEN}方式三：用列表推導式", result)

# 帶條件的列表推導式
nums = [10, 20, 30, 40]
result = [n * 2 for n in nums if n > 20]
print(f"{Fore.GREEN}帶條件的列表推導式", result)

# 字典推導式
names = ["張三", "李四", "王五"]
scores = [60, 70, 80]
result = {names[i]: scores[i] for i in range(len(names))}
print(f"{Fore.GREEN}字典推導式", result)

# 集合推導式
names = ["張三", "李四", "王五"]
result = {n + "！" for n in names}
print(f"{Fore.GREEN}集合推導式", result)

names = ["張三", "李四", "王五"]
# Python 中沒有元組推導式，下面這種寫法叫：生成器
result = (n + "！" for n in names)
print(f"{Fore.GREEN}生成器", result)
