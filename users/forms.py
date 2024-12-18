# users/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'whatsapp_number')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'whatsapp_number')


class ProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text="Format: YYYY-MM-DD"
    )

    class Meta:
        model = Profile
        fields = [
            'date_of_birth',
            'nationality',
            'phone_number',
            'address_line1',
            'address_line2',
            'city',
            'state',
            'country',
            'postal_code',
            'profile_picture'
        ]
        widgets = {
            'address_line1': forms.TextInput(attrs={'placeholder': 'Street address'}),
            'address_line2': forms.TextInput(attrs={'placeholder': 'Apartment, suite, etc.'}),
            'postal_code': forms.TextInput(attrs={'placeholder': 'Postal/ZIP code'}),
        }