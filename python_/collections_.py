from collections import namedtuple
person = namedtuple('Person', ['last_name', 'name'])
p = person('TESt', 'Test')
p = p._replace(name='DIMA')
iter(p)
print(p.last_name) # like getitem


##   EXAMPLE ####################
#
# import csv
# data = []
# for i in csv.reader(open('data.csv')):
#     data.append(i[-2:])
# for i in map(person._make, data):
#     print(i.name)

###############################


import heapq
xs = [(13, 'A'), (12, 'B')]
heapq.heapify(xs)
heapq.heappush(xs, (1,'a'))
print(xs)
print(heapq.heappop(xs)) # very lower element

print(*heapq.merge({8,7,5}, [1,3,2], [12], [0,1])) # collection
from itertools import chain
print(*sorted(chain({8,7,4}, [1,3,2]))) # element




from collections import deque
d = deque((1,2,3), maxlen=4)
d.append(2)
d.appendleft(10)
d.popleft()


from collections import defaultdict

d = defaultdict(int)
d[1]+= 10
#print(d[2]) ->  0

############  EXAMPLE ########################
d = defaultdict(list)
data = [*zip(['a', 'b', 'a', 'c', 'b'], [1,2,3,4,5])]

for key, val in data:
    d[key].append(val)

data = [*zip(['a', 'b', 'a', 'c', 'b'], [1,2,3,4,5])]

dic = defaultdict(lambda : 'STTRING')
dic.update({'I': 'Tomas'})
print('%(test)s + %(I)s' % dic)
##########################################

from collections import Counter

d = Counter(open('data.csv').read().split(','))
c = Counter(open('data.csv').read().split(','))
print(d)
print(d.most_common(1))
print(c.subtract(d))
print(d) # dont change
print(c) # change

print(d + c) # Сложение
print(d - c) # Разность
print(c & d) # Пересечение
print(d | c) # Обьединение

########################################

from  collections import UserDict

class MyDict(UserDict):

    def __setitem__(self, key, value): # Вызывается и от setdefault
        print('I call')
        super().__setitem__(key, value)


my = MyDict()
my.setdefault('23','233')
my['1'] = 2
my.update({'1': 24})