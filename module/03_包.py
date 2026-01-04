# 套件概述：
# 1.在 Python 中，【包含 __init__.py 的資料夾】就是一個套件（Package）。
# 2.我們通常會把【某個特定功能相關的所有模組】放入一個套件中。
# 3.使用套件可以進一步提升程式碼的：可維護性、可複用性，便於管理大型專案。

# 套件與模組的關係：
# 1.一個模組就是一個.py檔案 ，套件是用來「管理模組」的目錄(資料夾)。
# 2.一個套件中可以有多個模組，也可以有多個子套件。

# 套件的分類：
# Python 中的套件分為三類，分別是：標準函式庫套件、自訂套件、第三方套件。

# 套件命名注意點：
# 1.要符合識別符號命名規範。
# 2.套件名稱區分大小寫（建議全部使用小寫字母）
# 3.不要與標準函式庫套件同名。

# 1️⃣import 套件名稱.模組名稱
# import trade.order
# import trade.pay
#
# trade.order.create_order()
# trade.pay.wechat_pay()

# 2️⃣import 套件名稱.模組名稱 as 別名
# import trade.order as dd
# import trade.pay as zf
#
# dd.create_order()
# zf.wechat_pay()


# 3️⃣from 套件名稱.模組名稱 import 具體內容1, 具體內容2, ......
# from trade.order import max_order_amount, create_order
# from trade.pay import timeout, wechat_pay
#
# print(max_order_amount)
# print(timeout)
# create_order()
# wechat_pay()


# 4️⃣from 套件名稱.模組名稱 import 具體內容1 as 別名1, 具體內容2 as 別名2, ......
# from trade.order import max_order_amount as max_amt, create_order
# from trade.pay import timeout, wechat_pay as w_pay
#
# print(max_amt)
# print(timeout)
# create_order()
# w_pay()


# 5️⃣from 套件名稱.模組名稱 import *
# from trade.order import *
# from trade.pay import *
#
# # print(max_order_amount)
# create_order()
# cancel_order()
# show_info()
#
# print(timeout)
# wechat_pay()
# ali_pay()
# show_info()

# 6️⃣from 套件名稱 import 模組名稱
# from trade import order, pay
# order.create_order()
# pay.wechat_pay()

# 7️⃣from 套件名稱 import 模組名稱 as 別名
# from trade import order as dd, pay as p
# dd.create_order()
# p.wechat_pay()

# 關於 __init__.py 檔案：
# 1.__init__.py 是套件的初始化檔案，在套件被匯入時，__init__.py 會被自動呼叫
# 2.__init__.py 中可以編寫一些套件的初始化邏輯
# 3.__init__.py 中所定義的內容，會被【from 套件名稱 import *】形式全部引入
# 4.__init__.py 中也可以使用 __all__ 來控制套件中的哪些模組可以被【from 套件名稱 import *】引入


# 8️⃣from 套件名稱 import *
# from trade import *
# # print(a)
# # print(b)
# print(order.max_order_amount)
# order.create_order()
# print(pay.timeout)
# pay.wechat_pay()

# 9️⃣import 套件名稱
# import trade
# print(trade.a)
# print(trade.b)
# trade.order.create_order()
# trade.pay.wechat_pay()

# 測試一下引入子套件
# from trade.hello.h1 import say_hello
# say_hello()

# 演示一下标准库包的使用
from collections import Counter
names = ['张三', '李四', '王五', '李华', '张三', '李四', '张三', '王五']
result = Counter(names)
print(result)

