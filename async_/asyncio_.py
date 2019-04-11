import aiohttp
from itertools import count
# asyncio Фреймворк для создания событийных циклов



"""
Event loop берет из очереди первый task, у ассоциированной с этим task корутиной вызывается метод step
корутина выполняется. Если корутина вызвает другую корутину, то делегирующая корутина приостанавливает свое выполнение 
и контроль выполнения переходит в вызванную корутину, если корутина вызывает блокирующую функцию
(async with aiohttp.request ) то она так же приостонавливается но контроль выполнения возвращяестя в event loop.
Затем event loop берет из очереди следующую задачу и так далее. Когда event loop возвращается к первой задаче, то 
ассоциированная с текущими task корутина продолжает работу с того момента где она остановилась в прошлый раз ( like gen.)
"""



import asyncio
import request
#@asyncio.coroutine
async def task1():
    while True:
        print('Asynk')
        await asyncio.sleep(1) #yield from

#@asyncio.coroutine
async def task2():
    for i in count():
        print(i)
        await asyncio.sleep(1) #yield from
        print('-')


#@asyncio.coroutine
async def loop():

    task_1 = asyncio.ensure_future(task1()) # Обернул в экземпляр класса Task
    task_2 = asyncio.ensure_future(task2())

    await asyncio.gather(task_1, task_2) #yield from

# loop_ = asyncio.get_event_loop()
# loop_.run_until_complete(loop())
# loop_.close()

##############################  AIOHTTP   ################

import time
def save_file(data):
    name = 'upploads/file_img_%f.jpg' % time.time()
    with open(name, 'wb') as file:
        file.write(data)


async def loader(client, url):
    async with client.get(url, allow_redirects=True) as response:
        body = await response.read()
        save_file(body)



async def main():
    tasks = []
    url = 'https://loremflickr.com/320/240'
    async with aiohttp.ClientSession() as client:
        for i in range(10):
            tasks.append(asyncio.ensure_future(loader(client, url)))
        await asyncio.gather(*tasks)

# start = time.time()
# loop_ = asyncio.get_event_loop()
# loop_.run_until_complete(main())
# loop_.close()


async def request(i):
    async with aiohttp.request('GET', 'https://api.github.com/events') as response:
        print('Client', i)
        return response.headers.get('Date')
        print('Newer print')

async def main():
    tasks = [request(client) for client in range(10)]
    await asyncio.gather(*tasks)

# loop_ = asyncio.get_event_loop()
# loop_.run_until_complete(main())
#
# loop_.close()


async def main():
    tasks = [request(client) for client in range(10)]
    for i in asyncio.as_completed(tasks):
        print(await i)

#
# loop_ = asyncio.get_event_loop()
# loop_.run_until_complete(main())
# loop_.close()

######### rocket ######################



async def launc(n):
    for i in range(1, 4):
        print(i)
        await asyncio.sleep(1)
    print('Start %s' %n)
    return 'Return to rocet_loop'


async def rocet_loop():
    tasks = []
    for i in range(10000):
        tasks.append(asyncio.ensure_future(launc(i)))
    print(await asyncio.gather(*tasks))
#
# loop_ = asyncio.get_event_loop()
# loop_.run_until_complete(rocet_loop())
# loop_.close()

################################# server  async #############################


async def client(reader, writer):
    while True:
        data = await reader.read(100)
        writer.write(b'Echo =>' + data)
        await writer.drain()


# loop_ = asyncio.get_event_loop()
# loop_.run_until_complete(loop_.create_task(asyncio.start_server(client, '0.0.0.0', 8001)))
# loop_.run_forever()
###################################

##################### CHANGE CONTEXT ##############

async def one():
    for i in count():
        print('one')
        await two(i)
        print('three')
        await asyncio.sleep(1)
        print('five')
        print(10 * '-')


async def two(i):
    #return '(((((((('
    print('two')


async def three():
    while True:
        print('four')
        await asyncio.sleep(0.10)

async def future():
    #done, pending = await asyncio.wait([asyncio.ensure_future(three())])
    #print(done, pending)
    await asyncio.gather(asyncio.ensure_future(one()), asyncio.ensure_future(three()))

loop_ = asyncio.get_event_loop()


loop_.run_until_complete(future())
loop_.close()

######################### as_completed #######################################

async def aioget(i, client=None):
    if not client:
        async with aiohttp.request('GET', 'http://localhost/') as response:
            data = response.request_info
    else:
        async with client.get('http://localhost/') as response:
            data = response.request_info
    print(i)
    return data


async def concurent():
    tasks = [aioget(task) for task in range(5)]
    for one in asyncio.as_completed(tasks): # Выдает результы корутин по мере их выполнения
        print(await one)

################################### return_when  ##################################
from concurrent.futures import FIRST_COMPLETED

async def wait_():
    async with aiohttp.ClientSession() as client:
        tasks =[aioget(i, client) for i in range(10)]
        done, pend = await asyncio.wait(tasks, return_when=FIRST_COMPLETED) # Первый выполненый Task
        print(done.pop().result()) #Результат первой выполненой задачи
        for task in pend: # список всех ожидающих Tasks
            task.cancel()

#
# loop_ = asyncio.get_event_loop()
# loop_.run_until_complete(wait_())
# loop_.close()

############################### exeptions ############

async def error():
    raise RuntimeError

async def exe():
    done, p = await asyncio.wait([error()])
    print(done)
    try:
        print(done.pop().result()) # error from coroutin, если не поймаю в лупе, то выкинет наружу
    except Exception:
        print('Error')
#
# loop_ = asyncio.get_event_loop()
# loop_.run_until_complete(exe())
# loop_.close()
################################# Timeout #########################
import random

async def waiting(i):
    time = random.randrange(10)
    await asyncio.sleep(time)
    return i

async def timeout():
    tasks = [waiting(i) for i in range(100)]
    done, p = await asyncio.wait(tasks, timeout=1) # ВСе кто уложились в 1 секнду
    for task in done:
        print(task.result())
    for task in p:
        task.cancel()
    return 'OK'


# loop_ = asyncio.get_event_loop()
# print(loop_.run_until_complete(timeout()))
# loop_.close()
##########################################################################
print(100 * '-')

async def check_future(future):
    print(future)
    await asyncio.sleep(1)
    future.set_result('HI')


loop_ = asyncio.get_event_loop()
future = asyncio.Future() # Обьект, который исполняется и его выполнение еще не завершенно
print(loop_.create_task(check_future(future)))
print(loop_.run_until_complete(future))
print(future.result())

async def test_start(i):
    await asyncio.sleep(2)
    print('OK', i)
# Варианты запуска
# loop_.run_until_complete(test_start(1))
# print(1)
# loop_.run_until_complete(asyncio.ensure_future(test_start(1.2)))
# print(1.2)
# loop_.run_until_complete(asyncio.gather(*[test_start(2), test_start(2)]))
# print(2)
# loop_.run_until_complete(asyncio.gather(*[asyncio.ensure_future(test_start(3)) for _ in range(2)]))
# print(3)
# loop_.run_until_complete(asyncio.wait([asyncio.ensure_future(test_start(4)) for _ in range(2)]))
# print(4)
#
# loop_.close()

#######################  Sync function
import time
from concurrent.futures import ThreadPoolExecutor
from functools import partial

def sync(arg):
    for i in range(10):
        print(arg, i)
        time.sleep(0.5)
    return arg

async def async_2():
    for i in range(10):
        print(i, 'HI')
        await asyncio.sleep(1)

async def async_():
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        print(pool)
        result = await loop.run_in_executor(pool, partial(sync, 1)) #В отдельном потоке
        print(result)
        print("END")



loop_ = asyncio.get_event_loop()
loop_.run_until_complete(asyncio.gather(async_(), async_2()))
loop_.close()

################# future

import asyncio

def callback(f):
    print(f.result())


async def a():
    loop = asyncio.get_event_loop()
    f = loop.create_future()
    f.add_done_callback(callback)
    f.set_result('HI')
    await f


# loop = asyncio.get_event_loop()
# loop.run_until_complete(a())
# loop.close()
####################

import asyncio


async def set_after(fut, delay, value):
    await asyncio.sleep(delay)
    print('!!!!!!!')

    fut.set_result(value)


async def main():
    loop = asyncio.get_event_loop()

    fut = loop.create_future()
    fut.add_done_callback(lambda i: print(i, 'Callback'))

    t = asyncio.ensure_future(set_after(fut, 1, '... world'))  # add to event loop

    result = await fut
    print(result, t)


asyncio.get_event_loop().run_until_complete(main())