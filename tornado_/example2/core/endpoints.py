class BaseEndpoint:
    METHODS = ['get', 'post', 'delete', 'patch']

    def __init__(self, *args, **kwargs):
        pass

    # def get(self): # search
    #     pass
    #
    # def post(self): # add
    #     pass
    #
    # def delete(self): # delete
    #     pass
    #
    # def patch(self): # change
    #     pass

    def dispatch(self, method, request, *args, **kwargs):
        method = method.lower()
        if method in self.METHODS and hasattr(self, method):
            return getattr(self, method)(request, *args, **kwargs)
        else:
            raise NotImplementedError(f'Method {method} not implemented in endpoint {type(self).__name__}')


    @classmethod
    def get_endpoint(cls, *args, **kwargs):
        def inner():
            request = HttpRequest()
            request.path = self.scope.get('path')
            request.session = self.scope.get('session', None)

            request.META['HTTP_CONTENT_TYPE'] = 'application/json'
            request.META['HTTP_ACCEPT'] = 'application/json'

            for (header_name, value) in self.scope.get('headers', []):
                request.META[header_name.decode('utf-8')] = value.decode('utf-8')

            args, view_kwargs = self.get_view_args(action=action, **kwargs)

            request.method = self.actions[action]
            request.POST = json.dumps(kwargs.get('data', {}))
            if self.scope.get('cookies'):

    request.COOKIES = self.scope.get('cookies')
            self = cls(*args, **kwargs)
            return self
        return inner