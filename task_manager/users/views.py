from typing import Callable

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.utils.translation import gettext as _

from task_manager.mixins import AuthRequiredMixin, CheckSelfUserMixin
from task_manager.users.forms import UserCreateUpdateForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class UserCreateView(SuccessMessageMixin, CreateView):
    model: User = get_user_model()
    form_class: UserCreateUpdateForm = UserCreateUpdateForm
    template_name: str = "users/create.html"
    success_message: tuple = _("User successfully registered")


class UserListView(ListView):
    model: User = get_user_model()
    template_name: str = "users/index.html"
    fields: tuple = ("first_name", "last_name", "username", "password1", "password2")


class UserDeleteView(AuthRequiredMixin, SuccessMessageMixin, CheckSelfUserMixin, DeleteView):
    model: User = get_user_model()
    template_name: str = "users/delete.html"
    auth_required_message: tuple = _("You are not logged in! Please sign in")
    permission_denied_message: tuple = _("You can't delete another user")
    permission_denied_url: str = "users:main"
    success_message: tuple = _("User successfully deleted")
    success_url: Callable = reverse_lazy("users:main")


class UserUpdateView(AuthRequiredMixin, SuccessMessageMixin, CheckSelfUserMixin, UpdateView):
    model: User = get_user_model()
    form_class: UserCreateUpdateForm = UserCreateUpdateForm
    template_name: str = "users/update.html"
    auth_required_message: tuple = _("You are not logged in! Please sign in")
    permission_denied_message: tuple = _("You can't update another user")
    permission_denied_url: str = "users:main"
    success_message: tuple = _("User successfully updated")
    success_url: Callable = reverse_lazy("users:main")
