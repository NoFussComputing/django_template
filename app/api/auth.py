from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, get_authorization_header

from api.models.tokens import AuthToken



class TokenAuthentication(BaseAuthentication):

    def authenticate_header(self, request):
        return 'Token'


    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth:
            return None

        if len(auth) == 1:

            raise exceptions.AuthenticationFailed('Token header invalid')

        elif len(auth) > 2:

            raise exceptions.AuthenticationFailed('Token header invalid. Possibly incorrectly formatted')


        elif len(auth) == 2:

            try:

                provided_token: str = token.token_hash(auth[1].decode("utf-8"))

            except UnicodeError:

                raise exceptions.AuthenticationFailed('Invalid token header. Token string should not contain invalid characters.')


            for token in AuthToken.objects.filter():

                if token.token == provided_token:

                    user = token.user

                    return (user, provided_token)

        return None
