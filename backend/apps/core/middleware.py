import datetime
import json
import pytz
import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from gqlauth.models import RefreshToken


def encode_jwt(payload, secret=settings.SECRET_KEY):
    return jwt.encode(payload, secret, algorithm="HS256")


def decode_jwt(token, secret=settings.SECRET_KEY):
    return jwt.decode(token, secret, algorithms=["HS256"])


def recursive_lookup(key, dictionary):
    if key in dictionary:
        return dictionary[key]
    for k, v in dictionary.items():
        if isinstance(v, dict):
            result = recursive_lookup(key, v)
            if result:
                return result


def jwt_refresh_token_middleware(get_response):
    def middleware(request):
        """Append generated refresh_token to response object."""
        cookie_refresh_token = request.COOKIES.get('refresh-token')
        remove_cookie = False
        user = None

        if cookie_refresh_token:
            try:
                refresh_token = decode_jwt(cookie_refresh_token)
                instance = RefreshToken.objects.select_related('user').get(token=refresh_token['refresh-token'])
                now = pytz.utc.localize(datetime.datetime.now())
                if instance.created + settings.GRAPHQL_JWT['JWT_REFRESH_EXPIRATION_DELTA'] > now:
                    user = instance.user
                else:
                    remove_cookie = True
            except (jwt.InvalidTokenError, jwt.ExpiredSignatureError, jwt.DecodeError, jwt.InvalidSignatureError,
                    RefreshToken.DoesNotExist):
                remove_cookie = True

            if user:
                iat = int(datetime.datetime.utcnow().timestamp())
                exp = int(iat + settings.GRAPHQL_JWT['JWT_EXPIRATION_DELTA'].total_seconds())
                username_field = get_user_model().USERNAME_FIELD
                payload = {username_field: getattr(user, username_field), 'exp': exp, 'origIat': iat}
                new_token = encode_jwt(payload)
                print(request)
                # request.META['HTTP_AUTHORIZATION'] = f'JWT {new_token}'
                request.META['Authorization'] = f'JWT {new_token}'

        response = get_response(request)

        if hasattr(response, 'content'):
            str_content_response = response.content.decode()
            if 'registerUser' in str_content_response or 'loginAuthToken' in str_content_response:
                content_response = json.loads(str_content_response)
                result = recursive_lookup('refreshToken', content_response)

                if result:
                    token = result['token']
                    user = RefreshToken.objects.select_related('user').get(token=token).user
                    jwt_code = encode_jwt({'refresh-token': token})
                    response.set_cookie(
                        'refresh-token',
                        jwt_code,
                        max_age=60 * 60 * 24 * 5,
                        httponly=True,  # protects token from leaking
                        secure=not settings.DEBUG
                    )
                    response.set_cookie(
                        'userGroups',
                        '.'.join(user.groups.values_list('name', flat=True)),
                        max_age=60 * 60 * 24 * 5,
                        httponly=True,  # protects token from leaking
                        secure=not settings.DEBUG
                    )
                    if user.is_superuser:
                        response.set_cookie(
                            'superUser',
                            user.is_superuser,
                            max_age=60 * 60 * 24 * 5,
                            httponly=True,  # protects token from leaking
                            secure=not settings.DEBUG
                        )
            if 'logoutUser' in str_content_response or remove_cookie:
                response.delete_cookie('refresh-token')
                response.delete_cookie('userGroups')
                response.delete_cookie('superUser')

        return response

    return middleware
