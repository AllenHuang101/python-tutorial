# 模組概述：
# 1.在 Python 中，一個.py檔案就是一個模組（Module）。
# 2.模組中可以包含：變數、函式、類別、等很多內容。
# 3.通常把能夠實現某一特定功能的程式碼，集中放在一個模組中（模組就類似於一個工具箱）。
# 4.模組可以提高程式碼的可維護性 與 可複用性，還可以避免命名衝突。

# 模組的分類：
# Python 中的模組分為三類，分別是：標準函式庫模組、自訂模組、第三方模組。

# 模組命名注意點：
#  1.要符合識別符號命名規則
#  2.模組名稱（.py檔案名稱）區分大小寫
#  3.不要與標準函式庫模組同名（一旦同名，Python會優先引入標準函式庫模組）


# 常見的模組匯入方式：
# 1️⃣import 模組名稱
# import order
# import pay
#
# print(order.max_order_amount)
# order.create_order()
# order.cancel_order()
# order.show_info()
# print('*' * 10)
# print(pay.timeout)
# pay.wechat_pay()
# pay.ali_pay()
# pay.show_info()


# 2️⃣import 模組名稱 as 別名
# import order as dd
# import pay as zf
#
# print(dd.max_order_amount)
# dd.create_order()
# dd.cancel_order()
# dd.show_info()
# print('*' * 10)
# print(zf.timeout)
# zf.wechat_pay()
# zf.ali_pay()
# zf.show_info()

# 3️⃣from 模組名稱 import 具體內容1, 具體內容2, ......
# from order import max_order_amount, show_info
# from pay import wechat_pay, ali_pay
#
# print(max_order_amount)
# show_info()
# wechat_pay()
# ali_pay()


# 4️⃣from 模組名稱 import 具體內容1 as 別名1, 具體內容2 as 別名2, ......
# from order import max_order_amount as max_amt, show_info as show1
# from pay import timeout as tm, show_info as show2
# print(max_amt)
# print(tm)
# show1()
# show2()


# 5️⃣from 模組名稱 import *
# from order import *
# from pay import *
#
# max_order_amount = 10
#
# print(max_order_amount)
# create_order()
# cancel_order()
# show_info()
#
# print(timeout)
# wechat_pay()
# ali_pay()
# show_info()

# 關於__all__：
# ● 在 Python 模組中，可透過 __all__ 來控制【from 模組 import *】能匯入哪些內容。
# ● __all__ 的值可以是：列表、元組。
#
#
# 關於__name__:
# ● __name__是每個 Python 模組（.py檔案）都擁有的一個內建變數。
# ● 它的具體值取決於模組的執行方式：
#       1.作為主程式直接執行，__name__ 的值是 __main__
#       2.作為模組被匯入到其他程式中執行，__name__的模組的檔案名稱（不帶.py）。

import pay