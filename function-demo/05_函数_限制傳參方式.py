# 定義函式（使用 / 和 * 限制傳參方式）
# / 前的參數只能使用位置參數傳遞
# * 後的參數只能使用關鍵字參數傳遞
def greet(name, /, gender, *, age, height):
    print(f'我叫{name}，性別{gender}，年齡是{age}，身高是{height}cm')

# 正確示例
greet('Jeff', '男', age=18, height=172)
greet('Jeff', gender='男', age=18, height=172)

# 錯誤示例
# greet(name='張三', gender='男', age=18, height=172)
# greet('張三', '男', 18, height=172)
