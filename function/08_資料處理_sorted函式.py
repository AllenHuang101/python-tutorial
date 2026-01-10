# sorted 函式：對一組數據進行排序，返回一組新數據。
# 語法格式：sorted(可迭代物件, key=xxx, reverse=xxx)

# 數字排序
# nums = [30, 40, 20, 10]
# result = sorted(nums, reverse=True)
# print(result)

# 依照字串的長度排序
# names = ['python', 'sql', 'java']
# result = sorted(names, key=len, reverse=True)
# print(result)

# 根據字典中的某個欄位進行排序
persons = [
    {"name": "張三", "age": 15, "gender": "男"},
    {"name": "李四", "age": 17, "gender": "女"},
    {"name": "王五", "age": 19, "gender": "男"},
    {"name": "李華", "age": 20, "gender": "女"},
    {"name": "趙六", "age": 18, "gender": "女"},
    {"name": "孫七", "age": 16, "gender": "男"},
]
result = sorted(persons, key=lambda p: p["age"], reverse=True)
print(result)

# 我們之前講的 max 函式、min 函式，也可以傳遞 key 參數，用於設定篩選依據
result1 = max(persons, key=lambda p: p["age"])
result2 = min(persons, key=lambda p: p["age"])
print(result1)
print(result2)
