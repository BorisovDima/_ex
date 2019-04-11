import hashlib
import base64
import json
import hmac

from .models import JWTtoken

# header = { "alg": "HS256", "typ": "JWT"}
# payload = { "userId": "b08f86af-35da-48f2-8fab-cef3904660bd", 'exp': 60}


SECRET_KEY = '123456'


class SimpleJWT:
    HASH_FUNC = {"HS256": hashlib.sha256}

    def create_token(self, *args, **kwargs):
        raise NotImplementedError

    def encode(self, data):
        """ isinstance(data, dict)"""
        json_data = json.dumps(data)
        base = base64.b64encode(json_data.encode('utf-8'))
        return base.decode('utf-8')

    def generate_header(self, alg):
        header = {'alg': alg, "typ": "JWT"}
        return self.encode(header)

    def generate_payload(self, data):
        return self.encode(data)

    def generate_signature(self, header, payload, alg):
        unsignedToken = f'{header}.{payload}'
        signature = hmac.new(key=SECRET_KEY, msg=unsignedToken.encode(), digestmod=self.HASH_FUNC[alg]).hexdigest()
        return signature



    def verify_token(self, token):
        pass

    def generate_token(self, payload, alg="HS256"):
        header = self.generate_header(alg)
        payload = self.generate_payload(payload)
        signature = self.generate_signature(header, payload, alg)
        token = f'{header}.{payload}.{signature}'
        return token

    def save(self):
        pass