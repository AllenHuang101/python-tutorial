import time
import multiprocessing

def task(name: str, count: int):
    print(f"{name} - start") 
    result = 0
    for n in range(count):
        result += n
    time.sleep(10000)
    print(f"{name} - end with {result}")

def start_process_1():
    process = multiprocessing.Process(target=task, args=["A", 100])
    process.start()
    process.join()

    print("Main process end")

def start_process_2():
    args_list = [("A", 100), ("B", 200), ("C", 300)]
    processes = [multiprocessing.Process(target=task, args=[name, count]) for name, count in args_list]
    
    for p in processes:
        p.start()

    for p in processes:
        p.join()


    print("Main process end")
    
if __name__ == '__main__':
    # start_process_1()
    start_process_2()
    