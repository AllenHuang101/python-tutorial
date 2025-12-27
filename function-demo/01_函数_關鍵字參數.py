# 定義函式
def greet(name, gender, age, height):
    print(f'我叫{name}，性別{gender}，年齡是{age}，身高是{height}cm')

# 呼叫函式（使用關鍵字參數）
greet(name='Allen', gender='男', age=18, height=172)
greet(height=172, age=18, gender='男', name='Leo')
greet('Jenli', '男', height=172, age=18)