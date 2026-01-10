from colorama import Fore, init

init(autoreset=True)

# map函式：對一組資料中的每一個元素，統一執行某種操作（加工），並生成一組新資料。
# 語法格式：map(操作函式, 可迭代物件)

# 統一資料處理
print(Fore.GREEN + "統一資料處理")
nums = [10, 20, 30, 40]


def double(x):
    return x * 2


# map函式的返回值是一個迭代器物件,需要我們自己去手動遍歷，或者手動類型轉換
# result = map(double, nums)
result = map(lambda x: x * 2, nums)
print(result, list(result))
print(nums)

# 字串轉換
print(Fore.GREEN + "字串轉換")
names = ("python", "java", "js")
result = map(lambda x: x.upper(), names)
print(result, tuple(result))
print(names)

# 類型轉換
print(Fore.GREEN + "類型轉換")
str_number = {"1", "2", "3"}
result = map(int, str_number)
print(result, set(result))
print(str_number)

# 注意點：
# 1.延遲執行：map 不會立刻計算，只有在"需要結果"時才執行計算(迭代器)。
# 2.返回的是迭代器物件，且一旦遍歷完成，就會被"耗盡"。
# 3.map不會影響元素數量。

print(Fore.GREEN + "其他注意點")
nums = [10, 20, 30, 40]
result = map(lambda x: x * 2, nums)
print(list(result))
print(list(result))
nums = list(map(lambda x: x * 2, nums))
print(nums)
print(nums)
