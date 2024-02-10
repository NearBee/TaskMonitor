from django import forms
from django.forms import TextInput, EmailInput, PasswordInput

from .models import User


class UserRegistrationForm(forms.ModelForm):
    password_confirmation = forms.CharField(
        widget=PasswordInput(
            attrs={
                "class": "form-control mb-4 shadow-sm forminputBox",
                "id": "register_password_confirmation",
                "placeholder": "Confirm Password",
            }
        ),
        required=True,
        max_length=128,
    )

    class Meta:
        model = User
        fields = ["email", "password", "password_confirmation", "display_name"]
        widgets = {
            "password": PasswordInput(
                attrs={
                    "class": "form-control mb-4 shadow-sm forminputBox",
                    "id": "register_password",
                    "placeholder": "Password",
                },
            ),
            "email": EmailInput(
                attrs={
                    "class": "form-control mb-4 shadow-sm",
                    "id": "register_email",
                    "placeholder": "Email",
                }
            ),
            "display_name": TextInput(
                attrs={
                    "class": "form-control mb-2 shadow-sm",
                    "id": "register_display_name",
                    "placeholder": "Display name",
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


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "password"]
        widgets = {
            "email": EmailInput(
                attrs={
                    "class": "form-control mb-2 shadow-sm forminputBox",
                    "id": "login_email",
                    "placeholder": "Email",
                }
            ),
            "password": PasswordInput(
                attrs={
                    "class": "form-control mb-4 shadow-sm forminputBox",
                    "id": "login_password",
                    "placeholder": "Password",
                }
            ),
        }
