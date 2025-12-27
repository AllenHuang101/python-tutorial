# 定義函式（設定參數默認值）
# 默認參數必須放在必選參數的後面
# 默認參數後面所有的參數都必須是默認參數
# def greet(name, gender, age, msg='你好', height):  # 錯誤寫法
def greet(name, gender, age, height, msg='你好'):
    print(f'我叫{name}，性別{gender}，年齡是{age}，身高是{height}cm')
    print(f'我想說：{msg}')

# 呼叫函式
greet('張三', '男', 18, 172)
greet('張三', '男', 18, 172, 'hello')
greet('張三', '男', 18, 172, msg='hello')

