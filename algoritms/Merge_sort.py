from test_sort import test_sort
import random

# def merge_sort1(iterable):
#     if len(iterable) <= 1:
#         return iterable
#     slice_ = len(iterable) // 2
#     left = iterable[:slice_]
#     right = iterable[slice_:]
#     return merge(merge_sort(left), merge_sort(right))
#
# def merge(i1, i2):
#     result = []
#     n1 = n2 = 0
#     for i in i1:
#         for j in i2[n2:]:
#             if not i > j:
#                 result.append(i)
#                 n1 += 1
#                 break
#             else:
#                 n2 += 1
#                 result.append(j)
#     result.extend(i1[n1:] or i2[n2:])
#     return result




def merge_sort(iterable):
    if len(iterable) > 1:
        slice_ = len(iterable) // 2
        left = iterable[:slice_]
        right = iterable[slice_:]
        merge_sort(left)
        merge_sort(right)
        l1 = r2 = k = 0
        while l1 < len(left) and r2 < len(right):
            if not left[l1] > right[r2]:
                iterable[k] = left[l1]
                l1 += 1
            else:
                iterable[k] = right[r2]
                r2 += 1
            k += 1
        ost, n = (right, r2) if len(right) > r2 else (left, l1)
        while len(ost) > n:
            iterable[k] = ost[n]
            k += 1
            n += 1
    return iterable

import time
t = time.time()
for i in range(1000):
    iterable = random.choices(range(-1000, 1000), k=i)
    test_sort(iterable, merge_sort)
print(time.time() - t)