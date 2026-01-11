# 高階函式：當一個函式的『參數是函式』或者『返回值是函式』那該函式就是『高階函式』。

# 高階函式的意義：
# 1. 程式碼復用性高：可以把行為「獨立出去」，傳入不同函式實現不同邏輯。
# 2. 能讓函式更靈活，更通用。
# 3. 高階函式是：裝飾器、閉包的基礎。


def info(msg):
    return "[提示]：" + msg


def warn(msg):
    return "[警告]：" + msg


def error(msg):
    return "[錯誤]：" + msg


def log(func, text):
    print(func(text))


log(info, "檔案儲存成功！")
log(warn, "磁碟空間不足！")
log(error, "該使用者不存在！")
