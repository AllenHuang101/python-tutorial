from threading import Thread

def task(count: int):
    for n in range(count):
        print(n)

thread1 = Thread(name="t1", target=task, args=(10,))
thread2 = Thread(name="t2", target=task, args=(10,))

# 啟動線程
thread1.start()
thread2.start()

print("Waiting for threads to finish...")

# 等待線程結束
thread1.join()
thread2.join()

print("Main thread is end")