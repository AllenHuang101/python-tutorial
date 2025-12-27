# 變數型別註解：給變數加上型別說明，可增強程式碼的可讀性、讓 IDE 的提示更友好。
num: int = 100
prcie: float = 12.5
message: str = '你好啊'
is_vip: bool = True
result: None = None  # 語法上沒有問題，但這麼寫沒有意義

# 注意：可以先寫變數的型別註解，以後再賦值
# school: str
# print('*******', school)
# school = '尚硅谷'

# hobby 是列表，並且列表中的所有元素必須是 str 型別
hobby: list[str] = ['抽烟', '喝酒', '烫头']

# hobby 是列表，並且列表中的元素，可以是：str 或 int 型別
hobby: list[str | int] = ['抽烟', '喝酒', '烫头']
# 上面這行程式碼的舊寫法如下：
from typing import Union
hobby: list[Union[str, int]] = ['抽烟', '喝酒', '烫头']

# citys 是集合，並且集合中所有元素必須是 str 型別
citys: set[str] = {'北京', '上海', '深圳'}

# citys 是集合，並且集合中所有元素可以是：str 或 float 或 bool 型別
citys: set[str | float | bool] = {'北京', '上海', '深圳'}

# persons 是字典，鍵是 str 型別，值是 int 型別
persons: dict[str, int] = {'张三': 18, '李四': 19, '王五': 20}

# persons 是字典，鍵是 str 或 int 型別，值是 int 型別
persons: dict[str | int, int] = {'张三': 18, '李四': 19, '王五': 20}

# 元組的型別宣告有點特殊，各位要留意一下：
# scores 是元組，並且元組中僅包含1個int型別的元素
scores: tuple[int] = (60,)

# scores 是元組，並且元組中包含3個int型別的元素
scores: tuple[int, int, int] = (60, 70, 80)

# scores 是元組，並且元組中包含任意個數的元素，但每個元素的型別必須是int
scores: tuple[int, ...] = (60, 70, 80, 90, 100)

# scores 是元組，並且元組中包含任意個數的元素，每個元素的型別可以是：int 或 str
scores: tuple[int | str, ...] = (60, '70', 80, '90', 100)

# Python 會根據初始賦值推導變數的型別：
# 1. 對於普通變數：後續如果改變型別，不會警告。
# 2. 對於容器變數：要求內部元素型別必須與推導出來的一致，否則就會警告。
x = 100
x = '尚硅谷'

y = [10, 20, 30]
y.append('40')
