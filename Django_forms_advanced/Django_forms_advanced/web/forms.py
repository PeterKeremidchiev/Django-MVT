from django import forms
from django.core.exceptions import ValidationError
from django.forms import modelform_factory, modelformset_factory

from Django_forms_advanced.web.mixins import ReadonlyFieldsMixin
from Django_forms_advanced.web.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


    def clean(self):
        cleaned_data = super(PersonForm, self).clean()

        if cleaned_data['first_name'] == cleaned_data['last_name']:
            raise ValidationError('First and last name must be different')

        return cleaned_data


PersonForm2 = modelform_factory(Person, fields='__all__')

class UpdatePersonForm(ReadonlyFieldsMixin, PersonForm):
    readonly_fields = ('age',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._mark_readonly_fields()

PersonFormSet = modelformset_factory(Person, form=PersonForm, extra=1)