def hanoy(count, start='1', mid='2', end='3'):
    if count > 1:
        hanoy(count-1, start, end, mid)

    print(start, end)
    if count > 1:
        hanoy(count-1, mid, start, end)



