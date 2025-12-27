# 前置知識一：
# 1.每次呼叫函式時，Python 都會為函式建立一個新的局部作用域
# 2.函式執行完畢後，這個局部作用域會被銷毀，其中的局部變數也會隨之被釋放
# def outer():
#     num = 10
#     num += 1
#     print(num)
#
# outer()
# outer()
# outer()

# 前置知識二：
# 1.在 Python 中，【內層函式】可以存取其【外層函式】作用域中的變數
# 2.存取外層函式變數無需使用 nonlocal；但修改外層變數時要使用 nonlocal
# def outer():
#     num = 10
#
#     def inner():
#         nonlocal num
#         num = 99
#         print(1, num)
#     inner()
#     print(2, num)
#
# outer()


# 什麼是閉包？ ————  閉包 = 內層函式 + 被內層函式所引用的外層變數
# 閉包產生的條件：
#   1.要有函式嵌套。
#   2.在【內層函式】中，要存取【外層函式】的變數。
#   3.並且【外層函式】要傳回【內層函式】。———— 只有傳回了內層函式，閉包才能"活下來"
# def outer():
#     num = 10
#
#     def inner():
#         nonlocal num
#         num += 1
#         print(num)
#
#     return inner
#
# f = outer()
# f()
# f()
# f()

# 結論：
# 1.outer函式中，被inner所使用到的那些變數，會被封存到【閉包單元(cell)】中。
# 2.這些 cell 會組成一個 __closure__ 元組，最終放在了 inner 函式身上。

# 列印 __closure__ 元組
# print(f.__closure__)

# 列印 __closure__ 元組中的某一項
# print(f.__closure__[0])

# 列印 __closure__ 元組中的某一項的具體值
# print(f.__closure__[0].cell_contents)


# 注意點：
# 1. 呼叫n次外層函式，就會得到n個不同的閉包，並且這些閉包之間互不影響
# def outer():
#     num = 10
#
#     def inner():
#         nonlocal num
#         num += 1
#         print(num)
#
#     return inner
#
# f1 = outer()
# f1()
# f1()
# f1()
# print('*****************')
# f2 = outer()
# f2()


# 2. 內層函式中用到的外層變數是可變物件，多個閉包之間依然互不影響
# def outer():
#     nums = []
#
#     def inner(value):
#         nums.append(value)
#         print(nums)
#
#     return inner
#
# f1 = outer()
# f1(10)
# f1(20)
# f1(30)
# print('**********************')
# f2 = outer()
# f2(666)


# 閉包的優點：
# 1. 可以"記住"狀態：不用全域變數，也不用寫類別，就能在多次呼叫之間保存資料。
# 2. 可以做"配置過的函式"：先傳一部分參數，把環境固定住，得到一個定製版函式。
# 3. 可以實現簡單的"資料隱藏"：外層變數對外不可見，只能透過內層函式存取。
# 4. 是裝飾器（decorator）等高級用法的基礎。
# def beauty(char, n):
#     def show_msg(msg):
#         print(char * n + msg + char * n)
#     return show_msg
#
# show1 = beauty('*', 3)
# show1('你好啊')
# show1('尚硅谷')
#
# show2 = beauty('@', 5)
# show2('你好啊')
# show2('尚硅谷')

# 閉包的缺點：
# 1. 理解成本較高：對初學者不太友好，濫用會讓程式碼難讀。
# 2. 如果閉包裡引用了很大的物件，又長期不釋放，可能會增加記憶體佔用。
# 3. 很多場景下，其實用【類別 + 實例屬性】會更清晰，閉包不一定是最優解。
# class Beauty:
#     def __init__(self, char, n):
#         self.char = char
#         self.n = n
#
#     def show_msg(self, msg):
#         print(self.char * self.n + msg + self.char * self.n)
#
# b1 = Beauty('*', 3)
# b1.show_msg('你好啊')
# b1.show_msg('尚硅谷')
#
# b2 = Beauty('#', 5)
# b2.show_msg('你好啊')
# b2.show_msg('尚硅谷')