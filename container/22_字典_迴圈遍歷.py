# 字典不能使用while迴圈遍歷，但可以使用for迴圈遍歷
d1 = {'張三': 72, '李四': 60, '王五': 85}

for key in d1:
    print(f'{key}的成績是{d1[key]}')

for key in d1.keys():
    print(f'{key}的成績是{d1[key]}')