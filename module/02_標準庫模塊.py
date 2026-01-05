# 1.Python 中的模組分為三類，分別是：標準函式庫模組、自訂模組、第三方模組。
# 2.標準函式庫模組：隨著 Python 一起安裝在我們電腦上的那些模組。
# 3.有一些標準函式庫模組是用C語言實現的，這些用C語言實現的模組，又稱：【內建模組】。
# https://docs.python.org/zh-tw/3.14/tutorial/stdlib.html
# https://docs.python.org/zh-tw/3.14/py-modindex.html

from colorama import Fore, init

init(autoreset=True)

import copy  # 拷貝物件（淺拷貝、深拷貝）
import os  # 作業系統相關操作（檔案、資料夾、路徑系統層面的操作）
import random  # 隨機數相關（產生隨機數、隨機選擇、洗牌）

# print(copy.__file__)
# print(os.__file__)
# print(random.__file__)

# 如下的這些模組，屬於內建模組（C語言寫的，無法看到具體實現，也沒有__file__屬性）
import time  # 時間相關操作（取得時間、延時、格式化時間等。）
import math  # 數學相關（開平方、取絕對值 等等）
import sys  # Python 直譯器相關操作

# 建立一個資料夾
# os.mkdir('demo')

# 隨機選擇一個人
names = ["張三", "李四", "王五", "李華"]
# 從序列中回傳一個隨機元素
print(Fore.BLUE + "序列中回傳一個隨機元素:", random.choice(names))

# 洗牌
names = ["張三", "李四", "王五", "李華"]
# 將可變序列 x 原地 (in place) 隨機打亂位置
random.shuffle(names)
print(Fore.BLUE + "序列洗牌後的結果:", names)

# 休眠
# time.sleep(2)
# print('ok')

# 取得當前時間(時:分:秒)
print(Fore.BLUE + "當前時間:", time.strftime("%H:%M:%S"))
# 取得當前時間(%I 12 小時制 %p 上午/下午 時:分:秒)
print(Fore.BLUE + "當前時間:", time.strftime("%p %I:%M:%S"))

# 開平方
print(Fore.BLUE + "開平方:", math.sqrt(4))

# 取絕對值
print(Fore.BLUE + "取絕對值:", math.fabs(-11.2))

# 取得Python直譯器的版本
print(Fore.BLUE + "Python直譯器版本:", sys.version)
