# 1.函式也是物件
a1 = 100            # int類別的實例物件
a2 = 'hello'        # str類別的實例物件
a3 = [10, 20, 30]   # list類別的實例物件

def welcome():      # welcome函式function類別的實例物件
    print('你好啊')

print(type(a1))
print(type(a2))
print(type(a3))
print(type(welcome))

# 2.函式可以動態新增屬性
# def welcome():
#     print('你好啊')
# welcome.desc = '這是一個打招呼的函式'
# welcome.version = 1.0
# print(welcome.desc)
# print(welcome.version)


# 3.函式可以賦值給變數
# def welcome():
#     print('你好啊')
# welcome.desc = '這是一個打招呼的函式'
# welcome.version = 1.0
#
# say_hello = welcome
# say_hello()
# print(say_hello.desc)
# print(say_hello.version)


# 4.可變參數 vs 不可變參數
# 不可變參數
# a = 666
# def welcome(data):
#     print('data修改前', data, id(data))
#     data = 888
#     print('data修改後', data, id(data))
#
# print('函式呼叫前', a, id(a))
# welcome(a)
# print('函式呼叫後', a, id(a))

# 可變參數
# a = [10, 20, 30]
# def welcome(data):
#     print('data修改前', data, id(data))
#     data[2] = 99
#     print('data修改後', data, id(data))
#
# print('函式呼叫前', a, id(a))
# welcome(a)
# print('函式呼叫後', a, id(a))


# 5.函式也可以作為參數
# def welcome():
#     print('你好啊')
#
# def caller(f):
#     print('caller函式呼叫了')
#     f()
#
# caller(welcome)

# 6.函式也可以作為返回值
def welcome():
    print('你好啊')
    def show_msg(msg):
        print(msg)
    return show_msg

# result = welcome()
# result('尚矽谷')
welcome()('尚矽谷')

