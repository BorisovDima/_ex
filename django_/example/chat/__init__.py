from functools import partial

class j:
    @classmethod
    def l(cls):
        pass

class a(j):
    @classmethod
    def l(cls):
        print(cls)

class b(a):
    @classmethod
    def l(cls):
        print(super(b, cls).l())


class clm:
    def __init__(self, f):
        self.f = f
        print(f)

    def __get__(self, instance, owner):
        return partial(self.f, owner)

class l:
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        print('TUTA', args, kwargs)


class t:
    @clm
    def test(cls):
        print(cls)
    @l
    def dd(self):
        pass
t().dd()
