from django.shortcuts import render, redirect
from django.template.defaulttags import register
from django.db.models import Q
from .models import Resume, Education, SkillDescription, ResumeProjects, Hobby, References

from .forms import ResumeForm, EducationForm, SkillDescriptionForm, ResumeProjectsForm, HobbyForm, ReferencesForm


@register.filter(name='split')
def split(value, key):
    # value.split("key")
    return value.split(key)

# Create your views here.

# -------------------- resume section ----------------------- #


def home(request):
    search_query = request.GET.get('resume_search') if request.GET.get(
        'resume_search') != None else ''

    print(f"VAlue of search_query: {search_query}")

    resumes = Resume.objects.filter(

        Q(resume_title__icontains=search_query) |
        Q(resumeprojects__project_title__icontains=search_query) |
        Q(resumeprojects__technologies_used__icontains=search_query)

    )
    context = {
        "resumes": resumes
    }

    return render(request, "resume_generator/home.html", context)


def create_resume(request):
    form = ResumeForm()
    page = 'resume'
    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.profile = request.user.profile
            resume.save()
            return redirect("profile", request.user.profile.id)
    context = {
        "form": form,
        "page": page
    }
    return render(request, "resume_generator/forms.html", context)


def resume_detail_view(request, id):
    resume = Resume.objects.get(id=id)
    skill_summary = resume.skill_summary.split(".")
    context = {
        "resume": resume,
        "skill_summary": skill_summary

    }
    return render(request, "resume_generator/resume_detail.html", context)


def resume_update_view(request, id):
    resume = Resume.objects.get(id=id)
    if request.user.profile.id != resume.profile.id:
        return redirect("home")
    form = ResumeForm(instance=resume)
    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES, instance=resume)
        if form.is_valid():
            form.save()
            return redirect("resume_template_update_view", resume.id)

    context = {
        "form": form,
    }
    return render(request, "resume_generator/update_forms.html", context)


def resume_delete_view(request, id):
    resume = Resume.objects.get(id=id)
    if request.user.profile.id == resume.profile.id:
        resume.delete()
        return redirect("profile", request.user.profile.id)


# the following view is for updating resume template

def resume_template_update_view(request, id):
    resume = Resume.objects.get(id=id)
    skill_summary = resume.skill_summary.split(".")
    if request.user.profile.id != resume.profile.id:
        return redirect("home")
    context = {
        "resume": resume,
        "skill_summary": skill_summary

    }
    return render(request, "resume_generator/update_resume_template.html", context)

# ------------------- end of resume section ------------------ #


# --------------------- education section -------------------- #

def create_educational_detail(request):
    page = 'education'
    form = EducationForm()
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            education_form = form.save(commit=False)
            education_form.profile = request.user.profile
            education_form.save()
            return redirect("profile", request.user.profile.id)
    context = {
        'page': page,
        "form": form
    }
    return render(request, "resume_generator/forms.html", context)


def update_educational_detail(request, id):
    page = 'update education'
    education = Education.objects.get(id=id)

    if not request.user.profile.id == education.profile.id:
        return redirect("home")

    form = EducationForm(instance=education)
    if request.method == 'POST':
        update_object(request, EducationForm, form, education)
        return redirect("profile", request.user.profile.id)

    context = {
        'page': page,
        "form": form
    }
    return render(request, "resume_generator/update_forms.html", context)


def delete_educational_detail(request, id):
    education = Education.objects.get(id=id)
    if not request.user.profile.id == education.profile.id:
        return redirect("home")
    education.delete()
    return redirect("profile", request.user.profile.id)

# ------------------ end of education system ----------------- #


# ------------------ skill description section ----------------- #

def create_skill(request, id):
    resume = Resume.objects.get(id=id)
    page = "skill_description"
    form = SkillDescriptionForm()
    if request.method == "POST":
        create_object_with_resume_key(
            request, SkillDescriptionForm, form, resume)
        return redirect("resume_template_update_view", resume.id)
    context = {
        "form": form,
        "page": page
    }
    return render(request, "resume_generator/forms.html", context)


def update_skill(request, id):
    skill_description = SkillDescription.objects.get(id=id)
    page = "update_skill_description"
    if request.user.profile.id != skill_description.resume.profile.id:
        return redirect("home")
    form = SkillDescriptionForm(instance=skill_description)
    if request.method == "POST":
        update_object(request, SkillDescriptionForm, form, skill_description)
        return redirect("resume_template_update_view", skill_description.resume.id)

    context = {
        "form": form,
        "page": page
    }
    return render(request, "resume_generator/update_forms.html", context)


def delete_skill(request, id):
    skill_description = SkillDescription.objects.get(id=id)
    resume = skill_description.resume
    if request.user.profile.id != resume.profile.id:
        return redirect("home")
    skill_description.delete()
    return redirect("resume_template_update_view", resume.id)


# ------------------ end of skill description ------------------ #

# ------------------- resume projects section ------------------ #

def create_resume_project(request, id):
    resume = Resume.objects.get(id=id)
    page = "resume_projects"
    form = ResumeProjectsForm()
    if request.method == "POST":
        create_object_with_resume_key(
            request, ResumeProjectsForm, form, resume)
        return redirect("resume_template_update_view", resume.id)
    context = {
        "form": form,
        "page": page
    }
    return render(request, "resume_generator/forms.html", context)


def update_resume_project(request, id):
    resume_project = ResumeProjects.objects.get(id=id)
    page = "update_resume_projects"
    if request.user.profile.id != resume_project.resume.profile.id:
        return redirect("home")
    form = ResumeProjectsForm(instance=resume_project)
    if request.method == "POST":
        update_object(request, ResumeProjectsForm, form, resume_project)
        return redirect("resume_template_update_view", resume_project.resume.id)

    context = {
        "form": form,
        "page": page
    }
    return render(request, "resume_generator/update_forms.html", context)


def delete_resume_project(request, id):
    resume_project = ResumeProjects.objects.get(id=id)
    resume = resume_project.resume
    if request.user.profile.id != resume_project.resume.profile.id:
        return redirect("home")
    resume_project.delete()
    return redirect("resume_template_update_view", resume.id)


# ---------------- end of resume project section --------------- #

# ------------------------ hobby section ----------------------- #


def create_hobby(request, id):
    resume = Resume.objects.get(id=id)
    page = "hobby"
    form = HobbyForm()
    if request.method == "POST":
        create_object_with_resume_key(
            request, HobbyForm, form, resume)
        return redirect("resume_template_update_view", resume.id)
    context = {
        "form": form,
        "page": page
    }
    return render(request, "resume_generator/forms.html", context)


def update_hobby(request, id):
    hobby = Hobby.objects.get(id=id)
    page = "update_hobby"
    if request.user.profile.id != hobby.resume.profile.id:
        return redirect("home")
    form = HobbyForm(instance=hobby)
    if request.method == "POST":
        update_object(request, HobbyForm, form, hobby)
        return redirect("resume_template_update_view", hobby.resume.id)

    context = {
        "form": form,
        "page": page
    }
    return render(request, "resume_generator/update_forms.html", context)


def delete_hobby(request, id):
    hobby = Hobby.objects.get(id=id)
    resume = hobby.resume
    if request.user.profile.id != resume.profile.id:
        return redirect("home")
    hobby.delete()
    return redirect("resume_template_update_view", resume.id)


# -------------------- end of hobby section -------------------- #

# --------------------- references section --------------------- #

def create_reference(request, id):
    resume = Resume.objects.get(id=id)
    page = "references"
    form = ReferencesForm()
    if request.method == "POST":
        create_object_with_resume_key(
            request, ReferencesForm, form, resume)
        return redirect("resume_template_update_view", resume.id)
    context = {
        "form": form,
        "page": page
    }
    return render(request, "resume_generator/forms.html", context)


def update_reference(request, id):
    reference = References.objects.get(id=id)
    page = "update_references"
    if request.user.profile.id != reference.resume.profile.id:
        return redirect("home")
    form = ReferencesForm(instance=reference)
    if request.method == "POST":
        update_object(request, ReferencesForm, form, reference)
        return redirect("resume_template_update_view", reference.resume.id)

    context = {
        "form": form,
        "page": page
    }
    return render(request, "resume_generator/update_forms.html", context)


def delete_reference(request, id):
    reference = References.objects.get(id=id)
    resume = reference.resume
    if request.user.profile.id != resume.profile.id:
        return redirect("home")
    reference.delete()
    return redirect("resume_template_update_view", resume.id)

# ------------------ end of references section ----------------- #


def create_object_with_resume_key(request, formClass, form, resume_instance):
    form = formClass(request.POST)
    if form.is_valid():
        new_instance = form.save(commit=False)
        new_instance.resume = resume_instance
        new_instance.save()


def update_object(request,  formClass, form, instance):
    """
    Updates a model instance but one need to provide the request, FromClass, The Form itself and the model Instance
    """
    form = formClass(request.POST, instance=instance)
    if form.is_valid():
        form.save()
