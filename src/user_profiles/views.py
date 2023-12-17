from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm

# Create your views here.


def profile(request, id):
    profile = Profile.objects.get(id=id)
    context = {
        "profile": profile
    }
    return render(request, "user_profiles/user_profile.html", context)


def edit_profile(request, id):
    profile = Profile.objects.get(id=id)
    if (profile.id == request.user.profile.id):
        form = ProfileForm(instance=profile)
        if request.method == "POST":
            form = ProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                return redirect("profile", profile.id)
    else:
        return redirect("home")

    context = {
        "form": form,
    }
    return render(request, "user_profiles/edit_profile.html", context)
