import queue
import threading

q = queue.Queue()


def test(q):
    #q.get(block=False) raise Empty
    print(q.get())
    print(q.get())
    q.task_done()
    q.task_done()
    print(q.task_done.__doc__)
    for i in range(8):
        q.get()
        q.task_done()

threading.Thread(target=test, args=(q,)).start()

for i in range(10):
    q.put(i)
q.join()
print(q.join.__doc__)
