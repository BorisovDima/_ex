from test_sort import test_sort
import random

def shell_sort(iterable):
    n = len(iterable) // 2
    step = (n // 2) or 1
    while n:
        for i in range(step, len(iterable), step):
            for j in range(i, 0, -1*step):
                if iterable[j] < iterable[j - step]:
                    iterable[j], iterable[j - step] = iterable[j - step], iterable[j]
                else:
                     break
        n = n // 2
        step = step + n if n > 1 else 1
    return iterable

import time
t =  time.time()

for i in range(500):
    iterable = random.choices(range(-1000, 1000), k=i)
    test_sort(iterable, shell_sort)
print(time.time() - t)