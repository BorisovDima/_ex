import os

# Процесс связывается с открытым файлом с помощью fd который ему возвращает OC

fd = os.open(__file__, os.O_RDONLY) # We identify the file with the file descriptor that was returned by open()
print(fd)
fb = os.fdopen(fd) # Wrap to file obj
print(fb)