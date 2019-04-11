import json


def parse_message(msg):
    data_json = json.loads(msg)
    id = data_json.get('id')
    method = data_json.get('method')
    url = data_json.get('url')
    args = data_json.get('args')
    body = data_json.get('data')
    return id, method, url, args, body



