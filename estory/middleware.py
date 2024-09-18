from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.shortcuts import redirect

class LoginRequiredMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            # Loop through the list of prefixes and check if the request path starts with any of them
            for prefix in settings.LOGIN_REQUIRED_PATH_PREFIXES:
                if request.path.startswith(prefix):
                    return redirect(settings.LOGIN_URL)
        return None