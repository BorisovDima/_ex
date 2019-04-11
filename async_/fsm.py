import time
import heapq


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



