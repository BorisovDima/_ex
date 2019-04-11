def binary_search(goal, m, first, last):
    mid = (first + last) // 2
    if m[mid] == goal:
        return (True, mid)
    if first >= last:
        return (False, None)
    if m[mid] > goal:
        return binary_search(goal, m, first, mid-1)
    else:
        return binary_search(goal, m, mid+1, last)


list = [1,2,3,5,6,78,90,100]
mas = [1,2,3,4,5]
print(binary_search(2, mas, 0, len(mas)))
print(binary_search(78, list, 0, len(list)))

print(binary_search(2, list, 0, len(list)))



print(binary_search(90, list, 0, len(list)))

print(binary_search(0, list, 0, len(list)))

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(3, testlist,  0, len(testlist)))
print(binary_search(13,testlist,  0, len(testlist)))
