# 以下這五個函式：既能定義對應的【空容器】，又能將【其他類型】轉換為對應的資料類型

# 1.list 函式：1.定義空列表。2.將【可迭代物件】轉換為列表
# res1 = list(range(8))
# res2 = list('歡迎來到尚矽谷')
# res3 = list({10, 20, 30, 40, 50})
# res4 = list({'張三': 75, '李四': 60, '王五':85}.items())
# print(type(res1), res1)
# print(type(res2), res2)
# print(type(res3), res3)
# print(type(res4), res4)

# 2.tuple 函式：1.定義空元組。2.將【可迭代物件】轉換為元組
# res1 = tuple(range(8))
# res2 = tuple('歡迎來到尚矽谷')
# res3 = tuple({10, 20, 30, 40, 50})
# res4 = tuple({'張三': 75, '李四': 60, '王五':85})
# print(type(res1), res1)
# print(type(res2), res2)
# print(type(res3), res3)
# print(type(res4), res4)

# 3.set 函式：1.定義空集合。2.將【可迭代物件】轉換為集合
# res1 = set(range(8))
# res2 = set('歡迎來到尚矽谷')
# res3 = set({10, 20, 30, 40, 50})
# res4 = set({'張三': 75, '李四': 60, '王五':85})
# print(type(res1), res1)
# print(type(res2), res2)
# print(type(res3), res3)
# print(type(res4), res4)


# 4.str 函式：1.定義空字串。2.將【任意類型】轉換為字串
# res1 = str(range(8))
# res2 = str('歡迎來到尚矽谷')
# res3 = str({10, 20, 30, 40, 50})
# res4 = str({'張三': 75, '李四': 60, '王五':85})
# res5 = str(False)
# res6 = str(None)
# res7 = str(100)
# print(type(res1), res1)
# print(type(res2), res2)
# print(type(res3), res3)
# print(type(res4), res4)
# print(type(res5), res5)
# print(type(res6), res6)
# print(type(res6), res6)
# print(type(res7), res7)

# 5.dict 函式：1.定義空字典。2.將【可迭代物件】轉換為字典
# 備註：交給dict函式的內容必須是鍵值對才可以，否則就會報錯
# res1 = dict({'張三': 75, '李四': 60, '王五':85})
# res2 = dict([('張三', 75), ('李四', 60), ('王五', 85)])
# res3 = dict((('張三', 75), ('李四', 60), ('王五', 85)))
# res4 = dict({('張三', 75), ('李四', 60), ('王五', 85)})
# print(type(res1), res1)
# print(type(res2), res2)
# print(type(res3), res3)
# print(type(res4), res4)

# 所有的資料容器，都支援【成員運算符】： in / not in  作用：判斷某個"元素"是否在於容器中。
hobby = ['抽菸', '喝酒', '燙頭']
nums = (10, 20, 30, 40, 50)
message = 'hello,atgiugu'
citys = {'北京', '天津', '上海', '重慶'}
score = {'張三': 75, '李四': 60, '王五':85}

print('喝酒' not in hobby)
print(20 not in nums)
print('hel' not in message)
print('上海' not in citys)
print('李華' not in score)
