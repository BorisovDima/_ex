
def test_sort(iterable, func):
    sorted_p = sorted(iterable)
    sorted_a = func(iterable)
    assert sorted_p == sorted_a, (sorted_p, sorted_a)
    print('OK!')