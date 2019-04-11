from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
import asyncio

class AsyncAPI(APIView):

    @classmethod
    def as_view(cls, **initkwargs):
        async def endpoint(request, *args, **kwargs):
            self = cls()
            self.request = request
            try:
                method = getattr(self, request.method.lower(), None)
                request = self.initialize_request(request, *args, **kwargs)
                self.initial(request, *args, **kwargs)
                response = await method(request, *args, **kwargs)
            except Exception as exc:
                response = self.handle_exception(exc)
            return response

        return endpoint

