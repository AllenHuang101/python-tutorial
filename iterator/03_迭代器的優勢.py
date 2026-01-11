# 1. 迭代器是惰性計算，不會一次性產生所有結果，
#    因此能顯著降低記憶體佔用。
# 2. 當資料量很大，且不確定要使用多少結果時，
#    建議使用迭代器。
import time
import tracemalloc
from colorama import Fore, init

init(autoreset=True)


# 使用迭代器實作
# 產生 Fibonacci 1、 1、 2、 3、 5、 8、 13、 21、 34、 ...
class Fibo:
    def __init__(self, total):
        # 要產生多少個數
        self.total = total
        # 目前產生到第幾個（計數器、指標）
        self.index = 0
        # 初始的兩個值
        self.pre = 1
        self.cur = 1

    def __iter__(self):
        return self

    def __next__(self):
        # 當產生足夠數量後，拋出 StopIteration 例外
        if self.index >= self.total:
            raise StopIteration
        # 前兩項都是 1
        if self.index < 2:
            value = 1
        else:
            # 新的結果等於前兩項的和
            value = self.pre + self.cur
            # 更新 pre 和 cur
            self.pre = self.cur
            self.cur = value
        # 計數器 +1
        self.index += 1
        # 回傳 value
        return value


# 不使用迭代器的實作方式
def fibo(total):
    if total <= 0:
        return []
    if total == 1:
        return [1]
    nums = [1, 1]
    for i in range(2, total):
        nums.append(nums[-1] + nums[-2])
    return nums


# 查看記憶體佔用
tracemalloc.start()
f1 = Fibo(100000)
m = tracemalloc.get_traced_memory()[1]
print(f"{Fore.GREEN}迭代器記憶體佔用是：{m / 1024 / 1024}MB")

tracemalloc.start()
f1 = fibo(100000)
m = tracemalloc.get_traced_memory()[1]
print(f"{Fore.GREEN}非迭代器記憶體佔用是：{m / 1024 / 1024}MB")


time_1 = time.perf_counter()
f1 = Fibo(100000)
for n in f1:
    if n > 100:
        break
    print(n)
time_2 = time.perf_counter()
print(f"{Fore.GREEN}使用迭代器花費時間：{time_2 - time_1}秒")

time_1 = time.perf_counter()
f1 = fibo(100000)
for n in f1:
    if n > 100:
        break
    print(n)
time_2 = time.perf_counter()
print(f"{Fore.GREEN}使用迭代器花費時間：{time_2 - time_1}秒")
