import secrets
import jwt

'''
This module creates a JWT token

It imports the secrets and JWT modules, then defines the token payload,
after which it creates a secret key for token verification, and then
specify the algorithms allowed to decode the token.

Finally, it creates and prints the token
'''

payload = {
    'iss': 'auth.macs.com',
    'sub': 'macs',
    'aud': 'app-client',
    'exp': '1223120000',
    'iat': '1223100000',
    'role': 'admin'
}

secret = secrets.token_hex(32)
algos = ['HS512', 'HS256']

token = jwt.encode(payload, secret, algorithm='HS512')

print(token)