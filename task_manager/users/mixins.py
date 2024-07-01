from django.utils.translation import gettext as _


class CheckRelatedTasksMixin:
    def dispatch(self, request, *args, **kwargs):
        if (
            self.get_object().tasks_where_creator.all().exists()
            or self.get_object().tasks_where_executor.all().exists()
        ):
            return self.handle_no_permission(
                _("Unable to delete user because it is in use"), "users:main"
            )
        return super().dispatch(request, *args, **kwargs)
