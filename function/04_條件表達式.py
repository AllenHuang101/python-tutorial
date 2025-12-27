# 表達式：執行後能得到值的程式碼，就是表達式（表達式最終會形成一個值，可以寫在任何需要值的地方）。
# a1 = 3 + 5
# a2 = 'abc' * 3
# print(5 > 3)
# int('y' in 'python')
# a5 = len('hello')

# 條件表達式：根據條件的真假，在兩個值中二選一的表達式（又稱：三元表達式、三目運算符）。
age = 21

# 傳統的if-else去寫：
# if age >= 18:
#     text = '成年'
# else:
#     text = '未成年'
# print(text)

# 條件表達式去寫：值1 if 條件 else 值2
# text = '成年' if age >= 18 else '未成年'
# print(text)

# 條件表達式的使用場景：簡單的二選一場景
rain = True
eat = '外賣' if rain else '出去吃'

is_vip = False
disscount = 0.8 if is_vip else 1.0

is_login = False
msg = '歡迎回來！' if is_login else print('哈哈哈')

print(eat)
print(disscount)
print(msg)



