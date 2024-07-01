from django.utils.translation import gettext as _


class CheckRelatedTasksMixin:
    def dispatch(self, request, *args, **kwargs):
        if self.get_object().tasks.all().exists():
            return self.handle_no_permission(
                _("Unable to delete label because it is in use"), "labels:main"
            )
        return super().dispatch(request, *args, **kwargs)
