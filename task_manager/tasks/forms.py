import django.forms as forms

from task_manager.labels.models import Label
from task_manager.tasks.models import Task


class TaskCreateUpdateForm(forms.ModelForm):
    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
    )

    class Meta:
        model = Task
        fields = ("name", "description", "status", "executor", "labels")
