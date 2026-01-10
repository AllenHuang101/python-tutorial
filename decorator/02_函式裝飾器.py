# 裝飾器：
# 1.裝飾器是一種【可調用對象】（通常是函式），它能接收一個函式作為參數，並且會傳回一個新函數。
# 2.裝飾器可以在不修改原函式程式碼的前提下，增強或改變原函式的功能。

# 實際應用：在不改變原函式的前提下，給函式統一加上：日誌、計時、校驗、快取 等功能

# 關鍵點：
# 1.接收被裝飾的函式、同時傳回新函式（wrapper）
# 2.裝飾器"吐出來"的是 wrapper 函式，以後別人呼叫的也是 wrapper 函式。
# 3.為了保證參數的相容性，wrapper 函式要透過 *args 和 **kwargs 接收參數。
# 4.wrapper 函式中主要做的是：呼叫原函式（被裝飾的函式）、執行其它邏輯，但要記得將原函式的傳回值 return 出去。

from colorama import Fore, init

init(autoreset=True)


# 裝飾器
def say_hello(func):
    def wrapper(*args, **kwargs):
        print(Fore.BLUE + "裝飾器 Add->", "你好，我要開始計算了")
        return func(*args, **kwargs)

    return wrapper


# @say_hello 等同於 add = say_hello(add) 語法糖
@say_hello
def add(x, y):
    res = x + y
    print(Fore.GREEN + "原始函數功能 -> ", f"{x}和{y}相加的结果是：{res}")
    return res


def add2(x, y):
    res = x + y
    print(Fore.GREEN + "原始函數功能 -> ", f"{x}和{y}相加的结果是：{res}")
    return res


# 正常呼叫add函式
print(Fore.RED + "=======正常呼叫=======")
result = add2(10, 20)

# 需求：在不修改add函式的前提下，給add函式增加一些額外的功能，例如：計算前先列印一句歡迎語。
# 實現方案：使用裝飾器
# 下面這行程式碼，是手動裝飾，寫起來會麻煩一些，不推薦，推薦：@裝飾器名

print(Fore.RED + "=======手動裝飾=======")
add_pro = say_hello(add2)
result = add_pro(10, 20)

print(Fore.RED + "=======@裝飾器名=======")
result = add(10, 20)


# 進階：帶參數的裝飾器(三層嵌套，外層接收配置、中間層接收函式、內層接收具體參數)
def say_hello_with_params(msg):
    def outer(func):
        def wrapper(*args, **kwargs):
            print(f"你好，我要開始{msg}計算了")
            return func(*args, **kwargs)

        return wrapper

    return outer


# 裝飾加法跟減法 print 內容不一樣
@say_hello_with_params("加法")
def add3(x, y, z):
    res = x + y + z
    print(f"{x}和{y}和{z}相加的結果是：{res}")
    return res


@say_hello_with_params("減法")
def sub(x, y):
    res = x - y
    print(f"{x}和{y}相減的結果是：{res}")
    return res


print(Fore.RED + "=======裝飾器 with args=======")
result1 = add3(10, 20, 30)
# print(result1)

result2 = sub(20, 10)
# print(result2)


print(Fore.RED + "=======多個裝飾器=======")


# 進階：多個裝飾器一起使用
def test1(func):
    print("我是test1裝飾器")

    def wrapper(*args, **kwargs):
        print("test1追加的邏輯-before")
        res = func(*args, **kwargs)
        print("test1追加的邏輯-after")
        return res

    return wrapper


def test2(func):
    print("我是test2裝飾器")

    def wrapper(*args, **kwargs):
        print("test2追加的邏輯-before")
        res = func(*args, **kwargs)
        print("test2追加的邏輯-after")
        return res

    return wrapper


# test1(test2(add4))
@test1
@test2
def add4(x, y):
    res = x + y
    print(f"{x}和{y}相加的结果是{res}")
    return res


resuult = add4(10, 20)
# print(resuult)
