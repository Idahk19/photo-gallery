from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


from django import forms
from .models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'description', 'image', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg',
                'placeholder': 'Enter photo title'
            }),

            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg',
                'placeholder': 'Enter photo description',
                'rows': 4
            }),

            'image': forms.ClearableFileInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg'
            }),

            'tags': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg',
                'placeholder': 'e.g. nature, sunset, beach'
            }),
        }