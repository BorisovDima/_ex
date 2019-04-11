from test_sort import test_sort
import random

def selection_search(iteration):
    for n in range(len(iteration)-1):
        goal = 0
        for i in range(1, len(iteration)-n):
            if iteration[i] > iteration[goal]:
                goal = i
        iteration[i], iteration[goal] = iteration[goal], iteration[i]
    return iteration

import time
t =  time.time()

for i in range(500):
    iterable = random.choices(range(-1000, 1000), k=i)
    test_sort(iterable, selection_search)
print(time.time() - t)


