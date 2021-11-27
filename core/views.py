from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from core.models import Ticket
from review.models import Review
from userfollows.models import UserFollows
from .forms import NewTicketForm, NewUserForm
from django.shortcuts import get_list_or_404


# attention à ne filtrer les posts que de ceux que l'on suit

def home(request):
    if(request.user.is_authenticated):
        list_posts_and_reviews = []
        list_users_followed = get_list_or_404(
            UserFollows, user_id=request.user.id)
        list_reviews = Review.objects.all()
        list_posts = Ticket.objects.all()
        print(list_posts.__len__())
        for p in list_posts:
            for e in list_users_followed:
                for r in list_reviews:
                    if p.id == r.ticket_id and (r.user_id == request.user.id
                                                or r.user_id == e.followed_user_id
                                                or p.user_id == request.user.id
                                                or p.user_id == e.followed_user_id):
                        list_posts_and_reviews.append({"post": p, "review": None, "has_one": 1})
                        list_posts_and_reviews.append({"post": p, "review": r, "has_one": 1})
            if p.user_id == request.user.id:
                list_posts_and_reviews.append({"post": p, "review": None, "has_one": 0})
        return render(
            request=request,
            template_name="core/home.html",
            context={
                    'user_logged': request.user,
                    'posts_and_reviews': list_posts_and_reviews
            }
        )
    else:
        return redirect("logout")


def register_request(request):
    if request.method == "POST":
        register_form = NewUserForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(request.user.id)
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
    if(request.user.is_authenticated):
        return redirect("home")
    else:
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


def logout(request):
    if(request is not None):
        auth.logout(request)
    return redirect("connection")


def create_ticket(request):
    if request.method == "POST":
        ticket_form = NewTicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket_form.save(request.user.id)
            return redirect("posts")
    else:
        ticket_form = NewTicketForm()
        return render(
            request=request,
            template_name="ticket/ticket.html",
            context={"ticket_form": ticket_form})


def posts(request):
    if(request.user.is_authenticated):
        list_posts = []
        list_posts = Ticket.objects.filter(user_id=request.user.id)
        return render(
            request,
            template_name="ticket/list_tickets.html",
            context={
                    'my_posts': list_posts,
            })
    else:
        return redirect("logout")


def delete_ticket(request, post_id):
    post_to_del = Ticket.objects.get(id=post_id)
    post_to_id = post_to_del.user
    if(post_to_id == request.user):
        post_to_del.delete()
    return redirect("posts")


def update_ticket(request, post_id):
    post_to_modify = Ticket.objects.get(id=post_id)
    if request.method == "GET":
        ticket_form = NewTicketForm(instance=post_to_modify)
        return render(
            request=request,
            template_name="ticket/update_ticket.html",
            context={"ticket_form": ticket_form})
    elif request.method == "POST":
        ticket_form = NewTicketForm(request.POST, request.FILES, initial={
            "id": post_to_modify.id,
            "ticket": post_to_modify.ticket,
            "description": post_to_modify.description,
            "image": post_to_modify.image})
        if ticket_form.is_valid():
            post_to_modify.ticket = ticket_form.cleaned_data.get("ticket")
            post_to_modify.description = ticket_form.cleaned_data.get("description")
            post_to_modify.image = ticket_form.cleaned_data.get("image")
            post_to_modify.save()
        return redirect("posts")
