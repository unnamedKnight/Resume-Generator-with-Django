from django import forms
from .models import Resume, Education, SkillDescription, ResumeProjects, Hobby, References


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        exclude = ("profile",)
        help_texts = {
            "skill_summary": "At Most 200 Characters"
        }

    def __init__(self, *args, **kwargs):
        super(ResumeForm, self).__init__(*args, **kwargs)

        self.fields["resume_title"].widget = forms.TextInput(
            attrs={"class": "form-control"}
        )
        self.fields["resume_developer_role"].widget = forms.TextInput(
            attrs={"class": "form-control"}
        )
        self.fields["resume_short_intro"].widget = forms.Textarea(
            attrs={"class": "form-control",
                   "placeholder": "At Most 200 Characters"}
        )

        self.fields["skill_summary"].widget = forms.Textarea(
            attrs={"class": "form-control"}
        )

        self.fields["resume_image"].widget = forms.FileInput(
            attrs={"class": "form-control"}
        )


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        exclude = ("profile",)

    def __init__(self, *args, **kwargs):
        super(EducationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class SkillDescriptionForm(forms.ModelForm):
    class Meta:
        model = SkillDescription
        exclude = ("resume",)

    def __init__(self, *args, **kwargs):
        super(SkillDescriptionForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class ResumeProjectsForm(forms.ModelForm):
    class Meta:
        model = ResumeProjects
        exclude = ("resume",)

    def __init__(self, *args, **kwargs):
        super(ResumeProjectsForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class HobbyForm(forms.ModelForm):
    class Meta:
        model = Hobby
        exclude = ("resume",)

    def __init__(self, *args, **kwargs):
        super(HobbyForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class ReferencesForm(forms.ModelForm):
    class Meta:
        model = References
        exclude = ("resume",)

    def __init__(self, *args, **kwargs):
        super(ReferencesForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
