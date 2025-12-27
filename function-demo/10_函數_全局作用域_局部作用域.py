# 全域作用域 與 區域作用域，以及 global 的使用
a = 100
b = 200
c = 'ASUS'

def test():
    d = '你好啊'

    # Python 會創建一個局部變量 a 值為 300，這個 a 與全局變量 a 是不同的變量
    a = 300
    
    # 在函數中修改全局變量
    global b # 使用 global 關鍵字聲明 b 是全局變量
    b = 400
    
    print('函式中的輸出（a）', a)
    print('函式中的輸出（b）', b)
    print('函式中的輸出（c）', c)
    print('函式中的輸出（d）', d)

test()
print('***************')
print('全域的輸出（a）', a)
print('全域的輸出（b）', b)
print('全域的輸出（c）', c) 
# print(d)   # ⚠ 會報錯，因為 d 是函式內的區域變數


# 區域作用域 和 區域變數：在函式呼叫時建立，函式執行結束後自動銷毀
def test2():
    m = 100
    m += 1
    print(f'我是在 test2 函式中輸出的 m：{m}')

test2()
test2()
test2()


# 全域作用域 與 全域變數：程式開始時建立，程式結束時銷毀
n = 100
def test3():
    # 函數執行完，局部作用域內的局部變量就會被銷毀
    global n
    n += 1
    print(f'我是在 test3 函式中輸出的 n：{n}')
    
test3()
test3()
test3()
print(n)
