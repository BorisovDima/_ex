from test_sort import test_sort
import random



def insertion_search(iterable):
    for i in range(1, len(iterable)):
        for j in range(i, 0, -1):
            if iterable[j] > iterable[j-1]: break
            iterable[j], iterable[j-1] = iterable[j-1], iterable[j]
    return iterable


if __name__ == '__main__':
    import time

    t = time.time()

    for i in range(500):
        iterable = random.choices(range(-1000, 1000), k=i)
        test_sort(iterable, insertion_search)
    print(time.time() - t)

