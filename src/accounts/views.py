from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from user_profiles.models import Profile

User = get_user_model()
# Create your views here.
# def test(request):
#     return render(request, "accounts/test.html")


def user_registration(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            if not User.objects.filter(email=email).exists():
                user = User.objects.create_user(email=email)
                user.set_password(password)
                user.save()
                profile = Profile.objects.create(
                    full_name=form.cleaned_data["full_name"],
                    developer_role=form.cleaned_data["developer_role"],
                    email=user.email,
                    address=form.cleaned_data["address"],
                    user=user
                )
                profile.save()
                return redirect('user_login')
    context = {
        "form": form,
    }
    return render(request, "accounts/registration.html", context)


def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")

    return render(request, "accounts/login.html")


def user_logout(request):
    logout(request)
    return redirect("home")
