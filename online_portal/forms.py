from django.contrib.auth.models import User
from online_portal.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django import forms

# class RegistrationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = (
#                 'username',
#                 'first_name',
#                 'last_name',
#                 'email',
#                 'password1',
#                 'password2',
#                 )
#
class UpdateProfileForm(forms.ModelForm):
    username = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
    #
    # def clean_email(self):
    #     username = self.cleaned_data.get('username')
    #     email = self.cleaned_data.get('email')
    #
    #     if email and User.objects.filter(email=email).exclude(username=username).count():
    #         raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
    #     return email
    #
    # def save(self, commit=True):
    #     user = super(RegistrationForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #
    #     if commit:
    #         user.save()
    #
    #     return user

    # def save(self,commit = True):
    #     user = super(RegistrationForm , self).save(commit = False)
    #     user.first_name = cleaned_data['first_name']
    #     user.last_name = cleaned_data['last_name']
    #     user.email = cleaned_data['email']
    #
    #     if commit:
    #         user.save()
    #
    #     return user
#
class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = (

                'address',
        )
