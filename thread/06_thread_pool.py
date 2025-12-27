import time
from concurrent.futures import ThreadPoolExecutor

def task(name: str):
    print(f"{name} - step1")
    time.sleep(1)
    print(f"{name} - step2")

    return f"{name} - complete"

with ThreadPoolExecutor() as executor:
    result1 = executor.submit(task, 'A')
    result2 = executor.submit(task, 'B')
    print(result1.result(), result2.result())

with ThreadPoolExecutor() as executor:
    results = executor.map(task, ['C', 'D'])
    
    for r in results:
        print(r)