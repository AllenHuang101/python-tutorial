# 一、函式的多返回值
# def calculate(x, y):
#     res1 = x + y
#     res2 = x - y
#     return res1, res2
#
# result = calculate(30, 10)
# print(result)
#
# r1, r2 = calculate(30, 10)
# print(r1, r2)


# 二、參數的打包與解包

# 1.打包接收參數：
# *args    ：打包所有的位置參數（會形成一個元組）
# **kwargs ：打包所有的關鍵字參數（會形成一個字典）
# def show_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# show_info(10, 20, 30, name='張三', age=18, gender='男')


# 2.解包傳遞參數
# *變數名  ：將元組拆解成一個一個獨立的位置參數
# **變數名 ：將字典拆解一個一個 key=value 形式的關鍵字參數
# def show_info(num1, num2, num3, name, age, gender):
#     print(num1, num2, num3)
#     print(name, age, gender)
#
# nums = (10, 20, 30)
# person = {'name':'張三', 'age':18, 'gender':'男'}
#
# show_info(*nums, **person)


# 3.打包接收參數 和 解包傳遞參數 一起使用
# def show_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# nums = (10, 20, 30)
# person = {'name':'張三', 'age':18, 'gender':'男'}
#
# show_info(*nums, **person)

