from World_of_speed_app.core.utils import get_profile


class ReadOnlyMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        for field in form.fields.values():
            field.widget.attrs["readonly"] = "readonly"

        return form

class GetProfileObjectMixin:
    def get_object(self, queryset=None):
        return get_profile()


class GetCarContextDataMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile()
        return context