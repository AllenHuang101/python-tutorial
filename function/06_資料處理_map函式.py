# map函式：對一組資料中的每一個元素，統一執行某種操作（加工），並生成一組新資料。
# 語法格式：map(操作函式, 可迭代物件)

# 統一資料處理
# nums = [10, 20, 30, 40]
# map函式的返回值是一個迭代器物件,需要我們自己去手動遍歷，或者手動類型轉換
# result = map(lambda x: x * 2, nums)
# print(list(result))
# print(nums)

# 字串轉換
# names = ('python', 'java', 'js')
# result = map(lambda x: x.upper(), names)
# print(tuple(result))
# print(names)

# 類型轉換
# str_number = {'1', '2', '3'}
# result = map(int, str_number)
# print(set(result))
# print(str_number)

# 注意點：
# 1.延遲執行：map 不會立刻計算，只有在"需要結果"時才執行計算。
# 2.返回的是迭代器物件，且一旦遍歷完成，就會被"耗盡"。
# 3.map不會影響元素數量。

nums = [10, 20, 30, 40]
result = list(map(lambda x: x * 2, nums))
print(result)
print(result)
print(result)
print(result)