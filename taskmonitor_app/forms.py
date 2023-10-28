from django import forms
from django.forms import TextInput, EmailInput, PasswordInput

from .models import User


class user_registration_form(forms.ModelForm):
    class Meta:
        model = User
        fields = "username", "email", "password"
        widgets = {
            "username": TextInput(
                attrs={
                    "class": "form-control mb-4 shadow-sm forminputBox",
                    "id": "register_username",
                }
            ),
            "password": PasswordInput(
                attrs={
                    "class": "form-control mb-4 shadow-sm forminputBox",
                    "id": "register_password",
                }
            ),
            "email": EmailInput(
                attrs={
                    "class": "form-control mb-4 shadow-sm forminputBox",
                    "id": "register_email",
                }
            ),
        }
