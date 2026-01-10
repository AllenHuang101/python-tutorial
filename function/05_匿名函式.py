from colorama import Fore, init

init(autoreset=True)

# 概念：所謂『匿名函式』，就是沒有名字的函式，它無需使用 def 關鍵字去定義。
# 語法：Python 中使用 lambda 關鍵字來定義『匿名函式』，格式為：lambda 參數: 表達式
# 使用場景： 當一個函式只用一次、只做一點點小事，使用匿名函式會更簡潔。


# 使用普通函式實現計算效果
print(Fore.GREEN + "使用普通函式實現計算效果")


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def calculate(func, a, b):
    print(f"計算結果為：{func(a, b)}")


calculate(add, 30, 10)
calculate(sub, 30, 10)

# 匿名函式
print(Fore.GREEN + "匿名函式")
add1 = lambda x, y: x + y
add2 = lambda x: x + x
add3 = lambda: "我是add3函式"

result1 = add1(30, 10)
result2 = add2(30)
result3 = add3()
print(result1, result2, result3)


# 使用匿名函式實現計算效果
print(Fore.GREEN + "使用匿名函式實現計算效果")


def calculate2(func, a, b):
    print(f"計算結果為：{func(a, b)}")


calculate2(lambda x, y: x + y, 30, 10)
calculate2(lambda x, y: x - y, 30, 10)

# 注意點
# 1. 只能寫一行，不能寫多行程式碼。
# 2. 不能寫程式碼區塊（if、for、while）
# 3. 冒號右邊必須是表達式，且只能寫一個表達式。
# 4. 表達式結果自動作為返回值。

is_adult = lambda age: "成年" if age >= 18 else "未成年"
print(is_adult(18))
print(is_adult(13))
