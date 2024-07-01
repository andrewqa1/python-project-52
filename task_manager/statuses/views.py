from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.utils.translation import gettext as _

from task_manager.mixins import AuthRequiredMixin
from task_manager.statuses.forms import TaskStatusCreateUpdateForm
from task_manager.statuses.models import TaskStatus
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class TaskStatusCreateView(SuccessMessageMixin, CreateView, AuthRequiredMixin):
    model: TaskStatus = TaskStatus
    form_class: TaskStatusCreateUpdateForm = TaskStatusCreateUpdateForm
    template_name: str = "statuses/create.html"
    success_message: tuple = _("Status successfully created")


class TaskStatusListView(ListView, AuthRequiredMixin):
    model: TaskStatus = TaskStatus
    template_name: str = "statuses/index.html"


class TaskStatusUpdateView(AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    model: TaskStatus = TaskStatus
    form_class: TaskStatusCreateUpdateForm = TaskStatusCreateUpdateForm
    template_name: str = "statuses/update.html"
    auth_required_message: tuple = _("You are not logged in! Please sign in")
    success_message: tuple = _("Status successfully updated")
    success_url = reverse_lazy("statuses:main")


class TaskStatusDeleteView(AuthRequiredMixin, SuccessMessageMixin, DeleteView):
    model: TaskStatus = TaskStatus
    template_name: str = "statuses/delete.html"
    success_message: tuple = _("Status successfully deleted")
    success_url = reverse_lazy("statuses:main")
