from colorama import Fore, init

init(autoreset=True)

# filter 函式：從一組數據中，篩選出符合條件的元素（過濾），並組成一組新數據。
# 語法格式：filter(過濾函式, 可迭代物件)

# 篩選數值
print(Fore.GREEN + "篩選數值")
nums = [10, 20, 30, 40, 50]
result = filter(lambda n: n > 30, nums)
print(list(result))
print(nums)

# 篩選成年人
persons = [
    {"name": "張三", "age": 15, "gender": "男"},
    {"name": "李四", "age": 16, "gender": "女"},
    {"name": "王五", "age": 17, "gender": "男"},
    {"name": "李華", "age": 18, "gender": "女"},
    {"name": "趙六", "age": 19, "gender": "女"},
    {"name": "孫七", "age": 20, "gender": "男"},
]
result = filter(lambda p: p["age"] >= 18, persons)
print(list(result))

# 過濾非法字串
print(Fore.GREEN + "過濾非法字串")
names = ["張三", "", "李四", None, "王五"]
result = filter(lambda n: n, names)
print(list(result))

# 注意點
# 1. 延遲執行：filter 不會立刻篩選，只有在「需要結果」時才會執行。
# 2. 返回的是迭代器物件，而且一旦遍歷完成就會被「耗盡」。
# 3. filter 可能會影響元素數量。

print(Fore.GREEN + "特殊用法")
# filter 函式的特殊用法：如果不傳遞過濾函式，則會自動過濾掉「假值」
data = [0, 1, "", "hello", [], (), 5]
result = filter(None, data)
print(list(result))
