# reduce函式：將一組數據不斷「合併」，最終歸併成一個結果。
# 語法格式：reduce(合併函式, 可迭代物件, 初始值)。
# 備註：reduce函式需要從 functools 模組中引入才能使用。

# 從 functools 模組中引入 reduce
from functools import reduce

# 數值統計
# nums = [1, 2, 3, 4, 5]
# result = reduce(lambda a, b: a + b, nums, 10)
# print(result)

# 字串拼接
str_list = ['ab', 'cd', 'ef']
result = reduce(lambda a, b: a + b, str_list)
print(result)

