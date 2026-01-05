# 訂單最大金額
max_order_amount = 1000000

# 建立訂單
def create_order():
    print('訂單建立成功！')

# 關閉訂單
def cancel_order():
    print('訂單關閉成功！')

# 提示函式
def show_info():
    print('我是來自【訂單】模組的提示！')

# from order import * 時，只能匯入以下兩個內容 
# __all__ 只能限制 from 模組名稱 import * 的行為，對其他匯入方式無效
# __all__ = ['cancel_order', 'show_info']
