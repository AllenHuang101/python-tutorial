import time
from concurrent.futures import Future
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor


def func(value):
    time.sleep(1)
    print(value)


# 建立執行緒池
pool = ThreadPoolExecutor(max_workers=5)

# 建立行程池
# pool = ProcessPoolExecutor(max_workers=5)


for i in range(10):
    fut = pool.submit(func, i)
    print(fut)