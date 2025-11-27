from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from users.models import CustomUser


class UsernameAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # print(request.headers)
        username = request.headers.get("X-USERNAME")
        if not username:
            return None
        try:
            user = CustomUser.objects.get(username=username)
            return (user, None)
        except CustomUser.DoesNotExist:
            raise AuthenticationFailed(f"No user {username} found.")


# class CountryAuthentication(BaseAuthentication):  # not working ? > 작동이 되네..?
#     def authenticate(self, request):
#         country = request.headers.get("X-COUNTRY")
#         if not country:
#             return None
#         try:
#             all_user = CustomUser.objects.filter(country=country)
#             print(all_user)
#             return (all_user.first(), None)
#         except CustomUser.DoesNotExist:
#             raise AuthenticationFailed(f"No user {country} found.")
