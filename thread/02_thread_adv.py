import time
from threading import Thread

# 繼承 Thread 類別，建立自訂線程類別
class MyThread(Thread):
    def __init__(self, name: str, daemon: bool, count: int):
        super().__init__()
        # 若設定為守護線程，則主線程結束後，守護線程也會跟著結束
        # 守護現成一班用於非關鍵性任務，如日誌等
        self.daemon = daemon
        self.name = name
        self.count = count

    # 覆寫 run 方法，線程啟動後會執行此方法
    def run(self):
        for n in range(self.count):
            print(f"{self.name}: {n}")
            time.sleep(0.01)

t_1 = MyThread(name="A", daemon=False, count=10)
t_2 = MyThread(name="B", daemon=False, count=10)

t_1.start()
t_2.start()