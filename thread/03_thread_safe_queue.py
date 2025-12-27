from threading import Thread
from queue import Queue

class MsgProducer(Thread):
    def __init__(self, name: str, count: int, queue: Queue):
        super().__init__()
        self.name = name
        self.count = count
        self.queue = queue
   
    def run(self):
        for i in range(self.count):
            msg = f"{self.name} - {i}"
            # 將訊息放入佇列，若佇列已滿則等待
            self.queue.put(msg, block=True)

class MsgConsumer(Thread):
    def __init__(self, name: str, queue: Queue):
        super().__init__()
        self.name = name
        self.queue = queue
        self.daemon = True

    def run(self):
        while True:
            # 從佇列取出訊息，若佇列為空則等待
            msg = self.queue.get(block=True)
            print(f"{self.name} - {msg}")
            self.queue.task_done()

aueue = Queue(3)
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