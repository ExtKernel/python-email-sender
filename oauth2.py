import time

from functools import wraps
from flask import request
from jwt import decode, exceptions, PyJWKClient

from credentials import (
    OAUTH2_PROVIDER_URL,
    EXPECTED_ISSUER,
    EXPECTED_ROLE,
    CLIENT_ID
)

# Initialize PyJWKClient to fetch public keys
jwks_client = PyJWKClient(OAUTH2_PROVIDER_URL)


class InvalidClientId(Exception):
    pass


def verify_token(token):
    try:
        # Decode the token, skipping audience validation
        signing_key = jwks_client.get_signing_key_from_jwt(token)
        decoded_token = decode(token, signing_key.key, algorithms=['RS256'], options={'verify_aud': False})

        print()
        print(decoded_token)
        print()

        # Verify the issuer claim
        if decoded_token.get('iss') != EXPECTED_ISSUER:
            raise exceptions.InvalidIssuerError('Invalid issuer')

        # Verify the `exp` claim (expiration time)
        if decoded_token.get('exp') < time.time():
            raise exceptions.ExpiredSignatureError('Token expired')

        clients = decoded_token.get('resource_access', {})
        if CLIENT_ID not in clients:
            raise InvalidClientId('The token is issued for the wrong client. Client ID does not match')

        # Verify the user's role
        roles = decoded_token.get('realm_access', {}).get('roles', [])
        if (EXPECTED_ROLE not in roles) and (EXPECTED_ROLE not in clients.get(CLIENT_ID).get('roles', [])):
            raise exceptions.MissingRequiredClaimError(EXPECTED_ROLE)

        return decoded_token
    except exceptions.ExpiredSignatureError:
        return 'Token expired', 401
    except exceptions.MissingRequiredClaimError as e:
        return f'Invalid claims: {e}', 401
    except Exception as e:
        return f'Token verification failed: {e}', 401


def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
            verification_result = verify_token(token)
            if isinstance(verification_result, dict):
                return f(*args, **kwargs, user=verification_result)
            else:
                return verification_result
        else:
            return 'Missing or invalid token', 401

    return decorated_function
