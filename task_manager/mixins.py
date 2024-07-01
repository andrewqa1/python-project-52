from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.utils.translation import gettext as _


class InfoMessageMixin:
    message: str = ""

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, self.message)
        return super().dispatch(request, *args, **kwargs)


class AuthRequiredMixin(LoginRequiredMixin):
    auth_required_message: tuple = _("You are not logged in! Please sign in")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.auth_required_message)
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class CheckSelfUserMixin(UserPassesTestMixin):
    permission_denied_message: str = ""
    permission_denied_url: str = ""

    def test_func(self) -> bool:
        return self.get_object() == self.request.user

    def handle_no_permission(self):
        return redirect(self.permission_denied_url)

    def dispatch(self, request, *args, **kwargs):
        user_test_result = self.get_test_func()()
        if not user_test_result:
            messages.error(request, self.permission_denied_message)
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
