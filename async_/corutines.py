def corutine():
    """
    yield a(0)
    a +=  (yield) 122
    yield a(122)
    a +=  (yield) 10
    yield a(132)
    """
    a = 0
    while True:
        a += yield a
        print(a, '-')

d = corutine()
print(d.send(None))
print(d.send(122))
print(d.send(10))
#next(d) a + None
######################################

def corutin_error(n=0):
    while True:
        try:
            n = yield n
        except ArithmeticError as i:
            print(i, 'Send error')
            return 'Done' # info error

cor = corutin_error(10)
print(cor.send(None))
print(cor.send(10))
try:
    print(cor.throw(ArithmeticError)) # send error
except StopIteration as e:
    print(e.value)

print(100 * '=')
###########################################################
from functools import wraps

def corutine(gen):
    @wraps(gen)
    def wrap(*args, **kwargs):
        cor = gen(*args, **kwargs)
        print(next(cor))
        return cor
    return wrap

@corutine
def subgen():
    print('1')
    while True:
        try:
            msg = yield
            print(msg, '-')
            yield 10
        except RuntimeError:
            print('ERRO!!')
            break
    return 'END'

@corutine
def delegator(g):
    print(2)
    # while True:
    #     try:
    #         message = yield
    #         print('-')
    #         g.send(message)
    #     except Exception as i:
    #         g.throw(i)
    rerunt_ = yield from g # Делегирую подгенератору до return или стопитерейшион
    yield rerunt_

cor = delegator(subgen())
print(cor.send('NICE!')) #None
print(cor.send('NICE!')) #Good
print(cor.throw(RuntimeError))


