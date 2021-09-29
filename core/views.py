from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages


def home(request):
    return render(
        request=request,
        template_name="core/home.html")


def register_request(request):
    if request.method == "POST":
        register_form = NewUserForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
        return redirect("home")
    else:
        register_form = NewUserForm()
        return render(
            request=request,
            template_name="core/index.html",
            context={
                "register_form": register_form
                }
            )


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(
        request=request,
        template_name="core/index.html",
        context={"login_form": form}
        )


def connection(request):
    register_form = NewUserForm()
    login_form = AuthenticationForm(request, data=request.POST)
    return render(
        request=request,
        template_name="core/index.html",
        context={ 
                "register_form": register_form,
                "login_form": login_form
                }
            )
