# filter函式：從一組數據中，篩選出符合條件的元素（過濾），並組成一組新數據。
# 語法格式：filter(過濾函式, 可迭代物件)

# 篩選數值
# nums = [10, 20, 30, 40, 50]
# result = filter(lambda n: n > 30, nums)
# print(list(result))
# print(nums)

# 篩選成年人
# persons = [
#     {'name':'张三', 'age':15, 'gender':'男'},
#     {'name':'李四', 'age':16, 'gender':'女'},
#     {'name':'王五', 'age':17, 'gender':'男'},
#     {'name':'李华', 'age':18, 'gender':'女'},
#     {'name':'赵六', 'age':19, 'gender':'女'},
#     {'name':'孙七', 'age':20, 'gender':'男'}
# ]
# result = filter(lambda p: p['age'] >= 18, persons)
# print(list(result))

# 過濾一下非法字串
# names = ['张三', '', '李四', None, '王五']
# result = filter(lambda n: n, names)
# print(list(result))

# 注意点
# 1.延迟执行：filter不会立刻筛选，只有在“需要结果”时才执行。
# 2.返回的是迭代器对象，且一旦遍历完成就会被“耗尽”。
# 3.filter可能会影响元素数量。

# filter函数的特殊用法：如果不传递过滤函数，那么自动会过滤掉“假值”
data = [0, 1, '', 'hello', [], (), 5]
result = filter(None, data)
print(list(result))

