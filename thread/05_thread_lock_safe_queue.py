from threading import Thread, Condition

class SafeQueue:
    def __init__(self, size: int):
        self.__item_list = list()
        self.size = size
        self.__item_lock = Condition()

    def put(self, item):
        with self.__item_lock:
            while len(self.__item_list) >= self.size:
                self.__item_lock.wait()
                
            self.__item_list.insert(0, item)
            self.__item_lock.notify_all()

    def get(self):
        with self.__item_lock:
            while len(self.__item_list) == 0:
                self.__item_lock.wait()
            
            result = self.__item_list.pop()
            # 通知其他等待同一把鎖的執行緒
            self.__item_lock.notify_all()
            return result


class MsgProducer(Thread):
    def __init__(self, name: str, count: int, queue: SafeQueue):
        super().__init__()
        self.name = name
        self.count = count
        self.queue = queue
   
    def run(self):
        for i in range(self.count):
            msg = f"{self.name} - {i}"
            # 將訊息放入佇列，若佇列已滿則等待
            self.queue.put(msg)

class MsgConsumer(Thread):
    def __init__(self, name: str, queue: SafeQueue):
        super().__init__()
        self.name = name
        self.queue = queue
        # 所有非daemon執行緒結束後，daemon執行緒會自動結束
        self.daemon = True

    def run(self):
        while True:
            # 從佇列取出訊息，若佇列為空則等待
            msg = self.queue.get()
            print(f"{self.name} - {msg}")

aueue = SafeQueue(3)
threads = list()
threads.append(MsgProducer(name="P1", count=10, queue=aueue))
threads.append(MsgProducer(name="P2", count=10, queue=aueue))
threads.append(MsgProducer(name="P3", count=10, queue=aueue))

threads.append(MsgConsumer(name="C1", queue=aueue))
threads.append(MsgConsumer(name="C2", queue=aueue))

for t in threads:
    t.start()

# 等待所有生產者完成
for t in threads[:3]:
    t.join()