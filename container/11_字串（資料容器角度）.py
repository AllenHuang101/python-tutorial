# 字串的下標
# msg = 'welcome to atguigu'
# print(msg[3])
# print(msg[-1])

# 字串中的字符，不可修改
# msg = 'welcome to atguigu'
# msg[0] = 'a'

# 字串不能巢狀
# msg = 'welcome to'hello' atguigu'
# msg = 'welcome to"hello" atguigu'
# msg = 'welcome to\'hello\' atguigu'

# 常用方法
# index 方法：取得指定字元，在字串中第一次出現的下標
# msg = 'welcome to atguigu'
# result = msg.index('t')
# print(result)

# split 方法：將字串按照指定字元進行分隔，並將分隔後的內容存入一個列表
# msg  = '尚矽谷@atguigu@你好'
# result = msg.split('@')
# print(msg)
# print(result)

# msg  = 'welcome to atguigu'
# result = msg.split(' ')
# print(msg)
# print(result)

# replace 方法：將字串中的某個字元片段，替換成目標字串（不修改原字串，傳回新字串）
# msg = 'welcome to atguigu'
# result = msg.replace('atguigu', '尚矽谷')
# print(msg)
# print(result)

# count 方法：統計指定字元，在字串中出現的次數
# msg = 'welcome to atguigu'
# result = msg.count('g')
# print(result)

# strip 方法：從某個字串中刪除：指定字串中的任意字元
# 規則：從字串兩端開始刪除，直到遇到第一個不在字串中的字元就停下
# msg = '666尚6硅6谷666'
# result = msg.strip('6')
# print(msg)
# print(result)

# msg = '1234尚12硅34谷4321'
# result = msg.strip('1324')
# print(msg)
# print(result)

# msg = '34215尚12硅34谷4132'
# result = msg.strip('5432')
# print(msg)
# print(result)

# msg = '  尚矽谷  '
# result = msg.strip()
# print(msg)
# print(result)

# 常用內建函式
# len 函式：統計字串中字元的個數（字串長度）
# msg = 'welcome to atguigu'
# result = len(msg)
# print(result)

# 字串的迴圈遍歷
msg = 'welcome to atguigu'
# while迴圈遍歷
# index = 0
# while index < len(msg):
#     print(msg[index])
#     index += 1

# for迴圈遍歷
# for item in msg:
#     print(item)
