from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.utils.translation import gettext as _

from task_manager.labels.forms import LabelCreateUpdateForm
from task_manager.labels.models import Label
from task_manager.mixins import AuthRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class LabelCreateView(SuccessMessageMixin, CreateView, AuthRequiredMixin):
    model: Label = Label
    form_class: LabelCreateUpdateForm = LabelCreateUpdateForm
    template_name: str = "labels/create.html"
    success_message: tuple = _("Label successfully created")


class LabelListView(ListView, AuthRequiredMixin):
    model: Label = Label
    template_name: str = "labels/index.html"


class LabelUpdateView(AuthRequiredMixin, SuccessMessageMixin, UpdateView):
    model: Label = Label
    form_class: LabelCreateUpdateForm = LabelCreateUpdateForm
    template_name: str = "labels/update.html"
    success_message: tuple = _("Label successfully updated")
    success_url = reverse_lazy("labels:main")


class LabelDeleteView(AuthRequiredMixin, SuccessMessageMixin, DeleteView):
    model: Label = Label
    template_name: str = "labels/delete.html"
    success_message: tuple = _("Label successfully deleted")
    success_url = reverse_lazy("labels:main")
