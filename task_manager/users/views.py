from django.contrib.auth import get_user_model
from django.views.generic import CreateView, ListView, DeleteView
from django.utils.translation import gettext as _
from task_manager.users.forms import UserCreateForm
from django.contrib.messages.views import SuccessMessageMixin


class UserCreateView(SuccessMessageMixin, CreateView):
    model = get_user_model()
    form_class = UserCreateForm
    template_name = "users/create.html"
    success_message = _("User successfully registered")


class UserListView(ListView):
    model = get_user_model()
    template_name = "users/index.html"
    fields = ["first_name", "last_name", "username", "password1", "password2"]


# class UserDeleteView(DeleteView):
#     model = get_user_model()
#     template_name = "users/delete.html"
#