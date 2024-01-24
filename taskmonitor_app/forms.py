from django import forms
from django.forms import TextInput, EmailInput, PasswordInput

from .models import User


class user_registration_form(forms.ModelForm):
    password_confirmation = forms.CharField(
        widget=PasswordInput(
            attrs={
                "class": "form-control mb-4 shadow-sm forminputBox",
                "id": "register_password_confirmation",
                "placeholder": "Confirm Password",
            }
        ),
        required=True,
    )

    class Meta:
        model = User
        fields = "username", "password", "password_confirmation", "email"
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

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")

        if password and password_confirmation and password != password_confirmation:
            self.add_error("password_confirmation", "Passwords do not match")

        return cleaned_data
