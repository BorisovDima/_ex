import random
from test_sort import test_sort


def bubble_search(iteration):
    for n in range(1, len(iteration)):
        change = False
        for i in range(len(iteration)-n):
            if iteration[i] > iteration[i+1]:
                change = True
                iteration[i], iteration[i+1] = iteration[i+1], iteration[i]
        if not change:
            break
    return iteration

for i in range(500):
    iterable = random.choices(range(-100, 100), k=i)
    test_sort(iterable, bubble_search)


