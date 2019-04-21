import logging
from logging import handlers

root = logging.getLogger() # handle all childes
root.setLevel(logging.DEBUG)
h = logging.StreamHandler()
h.setLevel(logging.DEBUG)
h.setFormatter(logging.Formatter('I am root %(message)s'))
root.addHandler(h)

#################################################


l1 = logging.getLogger('log1')
l2 = logging.getLogger('log2')

l1.setLevel(logging.ERROR)
l2.setLevel(logging.DEBUG)

h1 = logging.StreamHandler()
h1.setLevel(logging.DEBUG)

h2 = logging.FileHandler('temp.log')
h2.setLevel(logging.ERROR)

l1.addHandler(h1)
l1.addHandler(h2)

l1.error('ERRRNO!')

#######################################

stream = logging.StreamHandler()
stream.setLevel(logging.DEBUG)
stream.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
l2.addHandler(stream)

l2.debug('DEB!')