def quick_sort(iterable):
    _quick_sort(iterable, 0, len(iterable)-1)
    return iterable

def _quick_sort(iterable, first, last):
    if last <= first: return
    leftmark = first+1
    rightmark = last
    while rightmark > leftmark or iterable[first] < iterable[rightmark]:
        if iterable[leftmark] < iterable[first]:
            leftmark += 1
        elif iterable[rightmark] < iterable[first]:
            iterable[leftmark], iterable[rightmark] = iterable[rightmark], iterable[leftmark]
            rightmark -= 1
            leftmark += 1
        else:
            rightmark -= 1
    iterable[rightmark], iterable[first] = iterable[first], iterable[rightmark]
    _quick_sort(iterable, first, rightmark-1) # left , 0, 2
    _quick_sort(iterable, rightmark+1, last) #right



import random
from test_sort import test_sort
import time
t =  time.time()

for i in range(1000):
    iterable = random.choices(range(-100, 100), k=i)
    test_sort(iterable, quick_sort)
print(time.time() - t)



