from threading import Thread, Lock

task_lock = Lock()

def task(name: str):
    for n in range(2):
        task_lock.acquire()
        print(f"{name} - round {n} - step1")
        print(f"{name} - round {n} - step2")
        print(f"{name} - round {n} - step3")
        task_lock.release()

t1 = Thread(target = task, args=("A",))
t2 = Thread(target = task, args=("B",))
t3 = Thread(target = task, args=("C",))

t1.start()
t2.start()
t3.start()
