import threading
import time

####################### very bad ######################
def started():
    time.sleep(1)
    for count in reversed(range(1, 4)):
        time.sleep(1)
        print('%d...' % count)
    print('Rocket launced!')


threads = []
for _ in range(1000):
    thread = threading.Thread(target=started, args=())
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()
print('END')

######################## automat  ##########################

import heapq

import time


def sleep(time):
    yield time

def generator(id, count, time):
    for i in range(count):
        print(i)
        yield from sleep(time)
    print('Rocket %s launched!' % id)

def fsm(count):
    """'start - когда ракета должна быть запущена, cur time + 1 секунда'"""
    now = time.time()
    works = [(start, id_, generator(id_, 3, 1)) for id_, (start,) in enumerate([(now,) for _ in range(count)])]
    heapq.heapify(works)
    while works:
        start, id_, launcher = heapq.heappop(works)
        start_up = start - time.time() # Пришло ли время запуска?
        if start_up > 0:
            time.sleep(start_up) # Если нет, то жду
        try:
            next_ = next(launcher)
        except StopIteration:
            continue
        heapq.heappush(works, (start+next_, id_, launcher)) # следующий запуск через секунду
fsm(10_000)


####################### asynk ############
import types
import heapq

@types.coroutine
def sleep(time):
    yield time

async def generator(id, count, time):
    for i in range(count):
        print(i)
        await sleep(time)
    print('Rocket %s launched!' % id)

def fsm(count):
    """'start - когда ракета должна быть запущена, cur time + 1 секунда'"""
    now = time.time()
    works = [(start, id_, generator(id_, 3, 1)) for id_, (start,) in enumerate([(now,) for _ in range(count)])]
    heapq.heapify(works)
    while works:
        start, id_, launcher = heapq.heappop(works)
        start_up = start - time.time() # Пришло ли время запуска?
        if start_up > 0:
            time.sleep(start_up) # Если нет, то жду
        try:
            next_ = launcher.send(None)
        except StopIteration:
            continue
        heapq.heappush(works, (start+next_, id_, launcher)) # следующий запуск через секунду


######################







##################################

@types.coroutine            # Not
def corutin_type():# НЕльзя юзать yield в async
   for i in range(10):
        yield i ** 2


async def corutin_(arg): # def
    print(arg)
    await corutin_type() #yield from


corut = corutin_('ARG')
print(corut.send(None)) #Next У асинхронных def отсутствует, но есть send как и у генераторов
print(corut.send(None))



