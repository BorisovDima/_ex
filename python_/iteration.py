


#  easy iter ##################

class list_:
    def __init__(self, value):
        self.item = []
        #self.index = 0
        for i in value:
            self.item.append(i)

    def __iter__(self):
        for i in self.item:
            yield i

   # def __iter__(self):
   #     return self

    #def __next__(self):
     #   try:
      #      value = self.item[self.index]
        #except IndexError:
       #     raise StopIteration
        #self.index += 1
        #return value

d = list_([1,2,3,4])

for i in d:
    #print(i)
    pass

for i in d:
    pass
    #print(i)

def chain_(*args):
    for xs in args:
        #for x in xs:
           # yield x     # instead yield from
        yield from xs

c,d = {1,2,3}, [1,2,3]

print(list(chain_(c,d)))

for i in chain_(c, d):
    print(i)
######################## ITERTOOLS ##############################

from itertools import islice

# map(len, ['a', 'ad'])[:2] not subscriptable

print(list(islice(map(len, ['1', '22', '333', '4444']), 1, 3))) # [2, 3]

def take(i, n):
    print(list(islice(i, 0, n)))

from itertools import count, cycle, repeat

take(count(start=10, step=2), 10) #infinity
print('count')

take(cycle(['1', '2', '3']), 10) # infinity
print('cycle')

print(*repeat(['12', 2], times=2))

from itertools import dropwhile, takewhile

print(*dropwhile(lambda a: a < 98, range(100))) # При False
print(*takewhile(lambda a: (a % 2) == 0, range(2, 100))) # ТОлько до первого False

generator = (i for i in count()) # without generate brake system (infinity)
print(*islice(generator, 2, 10))

from itertools import tee

a = s = iter(range(40, 50))
print(*a)
print(*s) #nothing

print(tee(range(2), 10))
a, b, c = tee(range(10), 3)
print(a)
print(*a, *b, *c)

from itertools import product, combinations

print(*product([1,2,3], [24, 34, 1, 3])) #Decart pr.
print(*product({1,2,3}, repeat=3))

print(*combinations([1,2,3,4], 3)) # combination without repeat

print(*combinations(enumerate('abc'), 2))

print(sum(1 for _ in range(100)))

from itertools import groupby

for i, f in groupby([1,2,3,4], lambda p: p>2):
    print(*f)


print([(''.join(g), i) for i, g in groupby('AAAABBBBSSSSSCCCCCAAAA@@@', key=lambda p: ord(p))])
#[('AAAA', 65), ('BBBB', 66), ('SSSSS', 83), ('CCCCC', 67), ('AAAA', 65), ('@@@', 64)]

############# Corutins ###############################

print(100 * '-')

def corutin(a, b):
    item = 0
    while True:
        print('-')
        #item = yield
        item += yield item ** 2


cor = corutin(1, 2)
print(cor.send(None))
print(cor.send(1))
print(cor.send(10))
print(cor.send(100))
print(cor.send(1000))
cor.close()
##################################
from functools import wraps


def corutine_start(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        gen = f(*args, **kwargs)
        next(gen)
        return gen
    return decorator

@corutine_start
def sum_corutin(s):
    item = 0
    while True:
        item += yield item ** s
        #return 'StopIteration --'



for i in range(2, 10):
    sum = sum_corutin(i)
    for i in [5,7,1]:
        print(sum.send(i))
    sum.close()

###########################################3

def test():
    for i in range(10):
        yield i


def testtest():
    # for x in xs:
    #     yield x     # instead yield from
    yield from test()
    yield 1

gen = testtest()

print(gen.send(None)) # like next()
print(next(gen))
print(gen.send(None))
#gen.throw(AttributeError)
gen.close() # close genrator


