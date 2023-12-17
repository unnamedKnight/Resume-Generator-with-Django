from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = "__all__"
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields["full_name"].widget = forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
        self.fields["developer_role"].widget = forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
        self.fields["short_intro"].widget = forms.Textarea(
            attrs={
                "class": "form-control",
            }
        )
        self.fields["phone_number"].widget = forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )

        self.fields["address"].widget = forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
        self.fields["profile_image"].widget = forms.FileInput(
            attrs={
                "class": "form-control",
            }
        )
        self.fields["fathers_name"].widget = forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
        self.fields["mothers_name"].widget = forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
        self.fields["date_of_birth"].widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "2000-01-20"
            }
        )
        self.fields["date_of_birth"].help_text = "You must add date in YYYY-MM-DD format"

        self.fields["religion"].widget = forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
        self.fields["nationality"].widget = forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
        self.fields["martial_status"].widget = forms.CheckboxInput(
            attrs={
                "class": "form-check-input",
            }
        )

    def clean_phone_number(self, *args, **kwargs):
        data = self.cleaned_data["phone_number"]
        if data == None or not len(data) > 11:
            raise forms.ValidationError("Please fill this field")
        return data

    def clean_fathers_name(self, *args, **kwargs):
        data = self.cleaned_data["fathers_name"]
        validate_field_not_empty(data)
        return data

    def clean_mothers_name(self, *args, **kwargs):
        data = self.cleaned_data["mothers_name"]
        validate_field_not_empty(data)
        return data

    def clean_date_of_birth(self, *args, **kwargs):
        data = self.cleaned_data["date_of_birth"]
        validate_field_not_null(data)
        return data

    def clean_religion(self, *args, **kwargs):
        data = self.cleaned_data["religion"]
        validate_field_not_empty(data)
        return data

    def clean_nationality(self, *args, **kwargs):
        data = self.cleaned_data["nationality"]
        validate_field_not_empty(data)
        return data


def validate_field_not_empty(data):
    if data == None or len(data) == 0:
        raise forms.ValidationError("Please fill this field")


def validate_field_not_null(data):
    if data == None:
        raise forms.ValidationError("Please fill this field")
