# 列表推導式：用一條簡潔語句，從可迭代物件中，生成新列表的語法結構。
# 備註：列表推導式本質上是對 for迴圈 + append() 的一種簡寫形式。
# 語法格式：[表達式 for 變數 in 可迭代物件]

# 需求：讓列表中每個元素，都變為原來的2倍，得到是一個新的列表

# 方式一：用map函数
# nums = [10, 20, 30, 40]
# result = list(map(lambda n: n * 2, nums))
# print(result)

# 方式二：用 for迴圈 + append()
# nums = [10, 20, 30, 40]
# result = []
# for n in nums:
#     result.append(n * 2)
# print(result)

# 方式三：用列表推导式
# nums = [10, 20, 30, 40]
# result = [n * 2 for n in nums]
# print(result)

# 帶條件的列表推導式
# nums = [10, 20, 30, 40]
# result = [n * 2 for n in nums if n > 20]
# print(result)

# 字典推導式
# names = ['张三', '李四', '王五']
# scores = [60, 70, 80]
# result = {names[i]: scores[i] for i in range(len(names))}
# print(result)

# 集合推導式
# names = ['张三', '李四', '王五']
# result = {n + '！' for n in names}
# print(result)

names = ['张三', '李四', '王五']
# Python中沒有元組推導式，下面這種寫法叫：生成器（後面會仔細講）
result = (n + '！' for n in names)
print(result)
