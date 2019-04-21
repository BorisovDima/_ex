from concurrent.futures import ThreadPoolExecutor
import threading
import time
import sys



def task(r):
    print('Done')
    time.sleep(2)
    print(len(sys._current_frames()))
    print(len(r))

class TestThread:
    MAX = 5
    pool = ThreadPoolExecutor(max_workers=MAX)

    def run(self):
        for i in range(10):
            r = open('thread.py').read()
            f = self.pool.submit(task, r)
            print('e')
        # self.pool.shutdown()  # True == wait
        print('Wai')

threading.Thread(target=TestThread().run).start()
print('ONe')

def _python_exit():
    pass