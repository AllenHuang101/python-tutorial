# 定義函式（使用 *args 接收：可變位置參數，參數名稱可以更改）
# args 中存放的是所有傳遞進來的位置參數，並且這些參數會被打包成一個元組
def testArgs(*args):
    print(args)
    
# 呼叫函式
testArgs('張三', '男', 18, 172)

# 定義函式（使用 **kwargs 接收：可變關鍵字參數，參數名稱可以更改）
# kwargs 中存放的是所有傳遞進來的關鍵字參數，並且這些參數會被打包成一個字典
def testKwargs(**kwargs):
    print(kwargs)
    
# 呼叫函式
# 會出錯
# testKwargs('張三', gender='男', age=18, height=172)
testKwargs(name='張三', gender='男', age=18, height=172)

# 可變位置參數 和 可變關鍵字參數 一起使用，但必須先寫可變位置參數
def testArgsAndKwargs(a, b, *args, c='ASUS', **kwargs):
    print('@@@@@@@@@@@@@@@@')
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
# 呼叫函式
testArgsAndKwargs('張三', '男', '抽煙', '喝酒', age=18, height=172)
