from colorama import Fore, init

init(autoreset=True)

print(Fore.GREEN + "=====1.函式也是物件=====")
# 1.函式也是物件
a1 = 100  # int類別的實例物件
a2 = "hello"  # str類別的實例物件
a3 = [10, 20, 30]  # list類別的實例物件


def welcome():  # welcome函式function類別的實例物件
    print("你好啊")


print(type(a1))
print(type(a2))
print(type(a3))
print(type(welcome))

print(Fore.GREEN + "=====2.函式可以動態新增屬性=====")


# 2.函式可以動態新增屬性
def welcome2():
    print("你好啊")


welcome2.desc = "這是一個打招呼的函式"
welcome2.version = 1.0
print(welcome2.desc)
print(welcome2.version)


print(Fore.GREEN + "=====3.函式可以賦值給變數=====")


# 3.函式可以賦值給變數
def welcome3():
    print("你好啊")


welcome3.desc = "這是一個打招呼的函式"
welcome3.version = 1.0

say_hello = welcome3
say_hello()
print(say_hello.desc)
print(say_hello.version)


print(Fore.GREEN + "=====4.不可變參數=====")
# 4.可變參數 vs 不可變參數
# 不可變參數
a = 666


def welcome4(data):
    print("data修改前", data, id(data))
    data = 888
    print("data修改後", data, id(data))


print("函式呼叫前", a, id(a))
welcome4(a)
print("函式呼叫後", a, id(a))

print(Fore.GREEN + "=====5.可變參數=====")
# 可變參數
a = [10, 20, 30]


def welcome5(data):
    print("data修改前", data, id(data))
    data[2] = 99
    print("data修改後", data, id(data))


print("函式呼叫前", a, id(a))
welcome5(a)
print("函式呼叫後", a, id(a))

print(Fore.GREEN + "=====5.函式也可以作為參數=====")


# 5.函式也可以作為參數
def welcome6():
    print("你好啊")


def caller(f):
    print("caller函式呼叫了")
    f()


caller(welcome6)

print(Fore.GREEN + "=====6.函式也可以作為返回值=====")


# 6.函式也可以作為返回值
def welcome7():
    print("你好啊")

    def show_msg(msg):
        print(msg)

    return show_msg


# result = welcome7()
# result('尚矽谷')
welcome7()("尚矽谷")
