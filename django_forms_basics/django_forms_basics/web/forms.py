from django import forms

from django_forms_basics.web.models import Employee


# class EmployeeForm(forms.Form):
#     INTERESTS = (
#         (1, 'Programming'),
#         (2, 'Design'),
#         (4, 'Gaming'),
#     )
#     first_name = forms.CharField(max_length=35, required=True, label='First name')
#     last_name = forms.CharField(max_length=35, required=True, label='Last name')
#     # role = forms.ChoiceField(choices=Employee.ROLES, required=False)
#     # interests = forms.IntegerField(widget=forms.CheckboxSelectMultiple(choices=INTERESTS), required=True)
#     email = forms.EmailField(required=True)

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'