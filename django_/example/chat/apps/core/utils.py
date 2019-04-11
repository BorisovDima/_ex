from django.urls import get_resolver, Resolver404
from django.http.request import HttpRequest
import json
from io import BytesIO
from contextlib import contextmanager
from django.contrib.auth import get_user_model
from urllib.parse import urlparse, parse_qs, splitquery
from django.http import QueryDict

def parse_msg(data_json):
    if isinstance(data_json, str):
        data_json = json.loads(data_json)
    id = data_json.get('id')
    method = data_json.get('method')
    url = data_json.get('url')
    params = data_json.get('params', {})
    body = data_json.get('data', {})
    headers = data_json.get('headers', {})
    return id, method, url, params, body, headers



@contextmanager
def error_handler(callback):
    # Call callback and put error
    try:
        yield
    except Exception as e:
        callback(e)


def get_endpoint(url):
    resolver = get_resolver()
    url = urlparse(url).path
    endpoint, args, kwargs = resolver.resolve(url)
    return endpoint, args, kwargs



def make_response(response, id):
    status_code = response.status_code
    data = response.data
    return {'status_code': status_code, 'data': data, 'id': id}


def make_request(scope, url, method, params, body, headers, **kwargs):
    path, query = urlparse(url).path, urlparse(url).query
    request = HttpRequest()
    request.path = path
    request.session = scope.get('session', None)
    content = json.dumps(body)

    request.META['HTTP_CONTENT_TYPE'] = 'application/json'
    request.META['HTTP_ACCEPT'] = 'application/json'
    request.META['HTTP_CONTENT_LENGTH'] = len(content)
    request.META['QUERY_STRING'] = query or ''

    request._read_started = False
    request._stream = BytesIO(content.encode('utf-8'))

    for (header_name, value) in scope.get('headers', []):
        request.META[header_name.decode('utf-8')] = value.decode('utf-8')

    query_s, data = QueryDict(query, mutable=True), QueryDict(mutable=True)
    print(params, query_s)
    query_s.update(params)
    data.update(body)

    request.method = method
    request.POST = data
    request.GET = query_s
    if scope.get('cookies'):
        request.COOKIES = scope.get('cookies')

    for k, v in headers.items():
        header = f'HTTP_{k.upper()}'
        request.META[header] = v.encode()

    if "server" in scope:
        request.META["SERVER_NAME"] = scope["server"][0]
        request.META["SERVER_PORT"] = scope["server"][1]
    else:
        request.META["SERVER_NAME"] = "localhost"
        request.META["SERVER_PORT"] = 80

    for k, v in kwargs.items():
        setattr(request, k, v)
    return request


def get_user():
    model = get_user_model()