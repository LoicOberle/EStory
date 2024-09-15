# myapp/middleware.py

from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.shortcuts import redirect

class LoginRequiredMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if not request.user.is_authenticated:
            if request.path.startswith(settings.LOGIN_REQUIRED_PATH_PREFIX):
                return redirect(settings.LOGIN_URL)
