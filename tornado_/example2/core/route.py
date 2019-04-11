
import re


class Route:

    def __init__(self):
        self.endpoints = {}

    def add_endpoint(self, path, endpoint):
        self.endpoints[path] = endpoint


    def resolve(self, path):
        for pattern, endpoint in self.endpoints.items():
            if isinstance(endpoint, type(self)) and path.startswith(pattern):
                return endpoint.resolve(path)
            regex = re.compile(pattern)
            if regex.match(path):
                return endpoint()




