s1 = {10, 20, 30, 40, 50, 60}

# 集合不能使用while迴圈遍歷（以下是錯誤範例）
# index = 0
# while index < len(s1):
#     print(s1[index])
#     index += 1

# 集合可以使用for迴圈遍歷
for item in s1:
    print(item)