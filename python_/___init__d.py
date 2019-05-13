import os

import time


if not os.fork():
    print(os.getpid())
    print(os.execlp('python', 'python', '__init__.py'))
    print(1000 * '-')
    print(os.getpid())
    os._exit(0)

os.wait()