from colorama import Fore, init

init(autoreset=True)

# 變數型別註解：給變數加上型別說明，可增強程式碼的可讀性、讓 IDE 的提示更友好。
num: int = 100
prcie: float = 12.5
message: str = "你好啊"
is_vip: bool = True
# 語法上沒有問題，但這麼寫沒有意義
result: None = None

# 注意：可以先寫變數的型別註解，以後再賦值
# python 沒有定義變量，賦值才會創建
school: str
# print("*******", school)
school = "尚硅谷"

# hobby 是列表，並且列表中的所有元素必須是 str 型別
# hobby: list = ["抽烟", "喝酒", "燙頭"]
hobby: list[str] = ["抽烟", "喝酒", "燙頭"]
# hobby.append(10)
print(f"{Fore.GREEN}hobby列表", hobby)

# hobby 是列表，並且列表中的元素，可以是：str 或 int 型別
hobby2: list[str | int] = ["抽烟", "喝酒", "燙頭"]
hobby2.append(10)
print(f"{Fore.GREEN}hobby2列表", hobby2)

# 上面這行程式碼的舊寫法如下：
from typing import Union

hobby3: list[Union[str, int]] = ["抽烟", "喝酒", "燙頭"]
print(f"{Fore.GREEN}hobby3列表", hobby3)

# citys 是集合，並且集合中所有元素必須是 str 型別
citys: set[str] = {"北京", "上海", "深圳"}
print(f"{Fore.GREEN}citys集合", citys)
# citys 是集合，並且集合中所有元素可以是：str 或 float 或 bool 型別
citys2: set[str | float | bool] = {"北京", "上海", "深圳"}
print(f"{Fore.GREEN}citys2集合", citys2)

# persons 是字典，鍵是 str 型別，值是 int 型別
persons: dict[str, int] = {"張三": 18, "李四": 19, "王五": 20}
persons["張三"] = 21
print(f"{Fore.GREEN}persons字典", persons)

# persons 是字典，鍵是 str 或 int 型別，值是 int 型別
persons2: dict[str | int, int] = {"張三": 18, "李四": 19, "王五": 20}
print(f"{Fore.GREEN}persons2字典", persons2)

# 元組的型別宣告有點特殊，各位要留意一下：
# scores 是元組，並且元組中僅包含「1」個int型別的元素
# 元組是不可變類型
scores: tuple[int] = (60,)
print(f"{Fore.GREEN}scores元組", scores)

# scores 是元組，並且元組中包含3個int型別的元素
scores2: tuple[int, int, int] = (60, 70, 80)
print(f"{Fore.GREEN}scores2元組", scores2)

# scores 是元組，並且元組中包含任意個數的元素，但每個元素的型別必須是int
scores3: tuple[int, ...] = (60, 70, 80, 90, 100)
print(f"{Fore.GREEN}scores3元組", scores3)

# scores 是元組，並且元組中包含任意個數的元素，每個元素的型別可以是：int 或 str
scores4: tuple[int | str, ...] = (60, "70", 80, "90", 100)
print(f"{Fore.GREEN}scores4元組", scores4)

# Python 會根據初始賦值推導變數的型別：
# 1. 對於普通變數：後續如果改變型別，不會警告。
# 2. 對於容器變數：要求內部元素型別必須與推導出來的一致，否則就會警告。
# x = 100
# x = "尚硅谷"

y = [10, 20, 30]
# y.append("40")
