# import time
# print('dadadada')
# import os
#
# print(os.getpid())


import sys
import os

# print(os.system('ssh borisov@192.168.5.128 '))

import os
def run(cmd,*args):
    pid, fd = os.forkpty()
    if pid==0: # child
        os.execlp(cmd,*args)
    while True:
        data = os.read(fd,1024)
        print(data)
        if b"password:" in data:    # ssh prompt
            os.write(fd,b"19960213\n")
        elif data.endswith(b"$ "):  # bash prompt for input
            os.write(fd,b"ls\n")
        #     os.write(fd,b"echo bye\n")
        #     os.write(fd,b"exit\n")
        # os.write(fd, b"ls\n")
run("ssh", "ssh", "borisov@172.16.128.130")



print(os.forkpty.__doc__)