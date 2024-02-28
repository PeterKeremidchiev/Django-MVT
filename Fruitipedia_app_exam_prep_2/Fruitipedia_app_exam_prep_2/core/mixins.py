from django import forms


class ProfileFormMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        form.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        form.fields['email'].widget.attrs['placeholder'] = 'Email'
        form.fields['password'].widget = forms.PasswordInput(attrs={
            'placeholder': 'Password'})
        form.fields['first_name'].label = ''
        form.fields['last_name'].label = ''
        form.fields['email'].label = ''
        form.fields['password'].label = ''

        return form

class FruitFormMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.fields['name'].widget.attrs['placeholder'] = 'Fruit Name'
        form.fields['image_url'].widget.attrs['placeholder'] = 'Fruit Image URL'
        form.fields['description'].widget.attrs['placeholder'] = 'Fruit Description'
        form.fields['nutrition'].widget.attrs['placeholder'] = 'Nutrition Info'
        form.fields['name'].label = ''
        form.fields['description'].label = ''
        form.fields['image_url'].label = ''
        form.fields['nutrition'].label = ''

        return form

class DisabledFormMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields['name'].disabled = True
        form.fields['description'].disabled = True
        form.fields['image_url'].disabled = True

        return form