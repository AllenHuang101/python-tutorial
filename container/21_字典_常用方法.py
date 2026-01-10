# keys方法：用於取得字典中所有的鍵
d1 = {"張三": 72, "李四": 60, "王五": 85}

# keys方法的傳回值不是list，而是一種叫做dict_keys的類型
result = d1.keys()
print(result)
print(type(result))

# dict_keys和列表類似，可以被遍歷，但要注意的是：它不能透過下標存取元素
for item in result:
    print(item)


# 借助內建的list函式，可以將dict_keys轉換成list
l1 = list(result)
print(l1)
print(type(l1))

# values方法：取得字典中所有的值
d1 = {"張三": 72, "李四": 60, "王五": 85}
# values方法的傳回值類型是：dict_values，它的特點和dict_keys一樣
result = d1.values()
print(result)
print(type(result))

# items方法：取得字典中所有的鍵值對（每組鍵值對以元組的形式呈現）
d1 = {"張三": 72, "李四": 60, "王五": 85}
# items方法傳回的類型是：dict_items，它的特點也和dict_keys一樣
result = d1.items()
print(result)
print(type(result))
