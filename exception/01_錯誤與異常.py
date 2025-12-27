# 錯誤：程式碼本身有語法錯誤，解譯器無法執行程式碼。———— 無法透過異常處理機制解決
# age = 18
# if age >= 18
#     print('成年人')

# 異常：程式碼在語法上沒問題，但執行過程中出現了問題。———— 可以透過異常處理機制解決
# 一些開發中常見的異常：

# 1.ZeroDivisionError：當除數為 0 時觸發。
# num1 = 100
# num2 = 0
# result = num1 / num2

# 2.TypeError：當操作的資料類型不正確或不相容時觸發。
# result = '10' + 5

# 3.AttributeError: 當物件沒有指定的屬性或方法時觸發。
# 展示1
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# p1 = Person('張三', 18)
# print(p1.name)
# print(p1.age)
# print(p1.gender)

# 展示2
# nums = [10, 20, 30]
# nums.add(40)

# 4.IndexError：當索引超出範圍（索引越界）時觸發。
# nums = [10, 20, 30, 40]
# print(nums[4])

# 5.NameError：當使用了不存在的變數時觸發。
# print(school)

# 6.KeyError：當存取字典中不存在的 key 時觸發。
# person = {'name':'張三', 'age':18}
# print(person['gender'])

# 7.ValueError：當值不合法，但類型正確時觸發。
# int('hello')


