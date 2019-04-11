def nod(a, b):
    one, two = (a, b) if a > b else (b, a)
    while one - two != 0:
        if one > two:
            one -= two
        else:
            two -= one
    return one


print(nod(105, 10))
