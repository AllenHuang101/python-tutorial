# 定義元組
# t1 = (28, 67, 21, 67, 11)
# t2 = ('北京', '尚矽谷', '你好')
# t3 = (100, True, '你好', None)
# t4 = (100, True, '你好', None, (50, 60, 70))
# print(type(t1), t1)
# print(type(t2), t2)
# print(type(t3), t3)
# print(type(t4), t4)

# 元組的下標
# t1 = (28, 67, 21, 67, 11)
# print(t1[3])
# print(t1[-1])

# 元組中的元素，不可修改
# t1 = (28, 67, 21, 67, 11)
# t1[0] = 100

# 元組中的元素，不可修改，但元組中如果存放了可變類型（列表），那可變類型中的內容仍可修改
# t2 = (28, 67, 21, 67, 11, [100, 200, 300, ('你好', '尚矽谷')])
# # t2[5] = 400
# t2[5][2] = 400
# t2[5][3][0] = 'hello'
# print(t2)

# 定義空元組
# t1 = ()
# t2 = tuple()
# print(type(t1), t1)
# print(type(t2), t2)

# 定義只有一個元素的元組
# t1 = ('你好',)
# t2 = (18,)
# print(type(t1), t1)
# print(type(t2), t2)

# 常用方法：
# index 方法：取得指定元素在元組中第一次出現的下標。
# t1 = (28, 67, 21, 67, 11)
# result = t1.index(67)
# print(result)

# count 方法：統計指定元素在元組中出現的次數。
# t1 = (28, 67, 21, 67, 11)
# result = t1.count(67)
# print(result)

# 常用內建函式
# max 函式，傳回元組中的最大值
# t1 = (23, 11, 32, 30, 17)
# result = max(t1)
# print(result)

# min 函式，傳回元組中的最小值
# t1 = (23, 11, 32, 30, 17)
# result = min(t1)
# print(result)

# len 函式，傳回元組中元素的個數（元組長度）
# t1 = (23, 11, 32, 30, 17)
# result = len(t1)
# print(result)

# sorted 函式，對元組進行排序（不修改原元組，返回一個新的列表）
# t1 = (23, 11, 32, 30, 17)
# result = sorted(t1, reverse=True)
# print(tuple(result))

# sum 函式，統計元組中所有元素的和（元素必須是純數字）
# t1 = (23, 11, 32, 30, 17)
# result = sum(t1)
# print(result)

# 實際開發中的元組，不一定是我們自己定義的，比如函式的可變參數*args就是一個元組
# def demo(*args):
#     return sum(args)
# result = demo(100, 200, 300)
# print(result)

# 元組的迴圈遍歷
t1 = (23, 11, 32, 30, 17)

# while迴圈遍歷
# index = 0
# while index < len(t1):
#     print(t1[index])
#     index += 1

# for迴圈遍歷
for item in t1:
    print(item)