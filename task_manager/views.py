from django.contrib.auth import views
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView
from django.utils.translation import gettext as _
from django.contrib import messages

from task_manager.mixins import CustomMessageMixin


class IndexView(TemplateView):
    template_name = "index.html"


class LoginView(SuccessMessageMixin, views.LoginView):
    template_name = "login.html"
    success_message = _("You are logged in")


class LogoutView(CustomMessageMixin, views.LogoutView):
    template_name = "logout.html"
    message = _('You are logged out')
