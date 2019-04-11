from contextlib import contextmanager
from docker.errors import APIError, NotFound, ImageNotFound

@contextmanager
def docker_exeptions():
    try:
        yield
    except (APIError, NotFound, ImageNotFound):
        pass