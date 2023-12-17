from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()


class RegistrationForm(UserCreationForm):
    full_name = forms.CharField()
    address = forms.CharField()
    developer_role = forms.CharField()

    class Meta:
        model = User
        fields = [
            "full_name",
            "address",
            "developer_role",
            "email",
        ]

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields["full_name"].widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Please enter your full name",
            }
        )
        self.fields["address"].widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Please enter your address"}
        )
        self.fields["developer_role"].widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Please enter your developer role",
            }
        )
        self.fields["email"].widget = forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Please enter your email"}
        )

        self.fields["password1"].widget = forms.PasswordInput(
            attrs={"class": "form-control"}
        )
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={"class": "form-control"}
        )
