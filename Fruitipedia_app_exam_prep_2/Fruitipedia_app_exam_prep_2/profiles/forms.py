# from Fruitipedia_app_exam_prep_2.profiles.models import Profile
# from django import forms
#
#
# class CreateProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('first_name', 'last_name', 'email', 'password')
#
#         widgets = {
#             'first_name': forms.TextInput(
#                 attrs={
#                     'placeholder': 'First Name',
#
#                 }
#             ),
#             'last_name': forms.TextInput(
#                 attrs={
#                     'placeholder': 'Last Name',
#                 }
#             ),
#             'email': forms.EmailInput(
#                 attrs={
#                     'placeholder': 'Email',
#                 }
#             ),
#             'password': forms.PasswordInput(
#                 attrs={
#                     'placeholder': 'Password',
#                 }
#             ),
#         }
#         labels = {
#             'first_name': '',
#             'last_name': '',
#             'email': '',
#             'password': '',
#         }