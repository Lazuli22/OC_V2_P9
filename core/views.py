from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages


def home(request):
    return render(
        request=request,
        template_name="core/home.html")


def connection(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
        return redirect("home")
    else:
        register_form = NewUserForm()
        login_form = AuthenticationForm(request, data=request.POST)
        return render(
            request=request,
            template_name="core/index.html",
            context={ 
                "register_form": register_form,
                "login_form": login_form}
            )
