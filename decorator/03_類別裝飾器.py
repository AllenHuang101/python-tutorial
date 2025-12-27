# 類別裝飾器：
# 1.包含 __call__ 方法的類別，就是類別裝飾器。
# 2.像呼叫函式一樣，去呼叫類別裝飾器的實例物件，就會觸發 __call__ 方法的呼叫。
# 3.__call__ 方法通常接收一個函式作為參數，並且會傳回一個新函式。

from colorama import Fore, init

init(autoreset=True) 

class SayHello:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print('你好，我要開始計算了')
            return func(*args, **kwargs)
        return wrapper

# 使用@語法糖使用類別裝飾器
@SayHello()
def add(x, y):
    res = x + y
    print(f'{x}和{y}相加的结果是{res}')
    return res

def add2(x, y):
    res = x + y
    print(f'{x}和{y}相加的结果是{res}')
    return res

print(Fore.RED + "=======手動裝飾=======")

# 使用 SayHello 去裝飾 add 函式（手動裝飾）
say = SayHello()
add2 = say(add2)
result = add2(10, 20)
# print(result)

print(Fore.RED + "=======使用類裝飾器=======")
result = add(10, 20)
# print(result)

# 帶參數的類別裝飾器
class SayHello2:
    def __init__(self, msg):
        self.msg = msg

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f'你好，我要開始{self.msg}計算了')
            return func(*args, **kwargs)
        return wrapper

@SayHello2('加法')
def add3(x, y):
    res = x + y
    print(f'{x}和{y}相加的结果是{res}')
    return res

print(Fore.RED + "=======帶參數的類裝飾器=======")
result = add3(10, 20)
print(result)


# 多個類別裝飾器的使用
class Test1:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print('我是Test1追加的邏輯')
            return func(*args, **kwargs)
        return wrapper

class Test2:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print('我是Test2追加的邏輯')
            return func(*args, **kwargs)
        return wrapper
    
print(Fore.RED + "=======多個類裝飾器=======")

@Test1()
@Test2()
def add4(x, y):
    res = x + y
    print(f'{x}和{y}相加的结果是{res}')
    return res

result = add4(10, 20)
print(result)

