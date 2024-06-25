from django.contrib import messages


class InfoMessageMixin:
    message: str = ""

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, self.message)
        return super().dispatch(request, *args, **kwargs)
