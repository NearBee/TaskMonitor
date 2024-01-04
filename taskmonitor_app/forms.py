from django import forms
from django.forms import TextInput, EmailInput, PasswordInput

from .models import User


class user_registration_form(forms.ModelForm):
    class Meta:
        model = User
        fields = "username", "password", "email"
        widgets = {
            "username": TextInput(
                attrs={
                    "class": "form-control mb-2 shadow-sm forminputBox",
                    "id": "register_username",
                    "placeholder": "Username",
                }
            ),
            "password": PasswordInput(
                attrs={
                    "class": "form-control mb-4 shadow-sm forminputBox",
                    "id": "register_password",
                    "placeholder": "Password",
                },
            ),
            "email": EmailInput(
                attrs={
                    "class": "form-control mb-4 shadow-sm forminputBox",
                    "id": "register_email",
                    "placeholder": "Email",
                }
            ),
        }
