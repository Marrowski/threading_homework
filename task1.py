import concurrent.futures
import threading
from concurrent.futures import ThreadPoolExecutor
import time

start = time.time()
def calculate_factorial(n):
    if n == 1:
        return 1
    elif n == 0:
        print('Zero num.')
    return calculate_factorial(n - 1) * n


end = time.time() - start

thread1 = threading.Thread(target= lambda: calculate_factorial(21))
thread1.start()
print(f'Time of executing function: {end}')


start = time.time()
def concurrent_factorial(n):
    if n == 1:
        return 1
    elif n == 0:
        print('Zero num.')
    return concurrent_factorial(n - 1) * n

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    future = executor.submit(concurrent_factorial, 21)
    result = future.result()

end_a = time.time() - start

print(f'Time of executing function with PoolExecutor: {end_a}')