from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from core.models import Ticket
from review.models import Review
from userfollows.models import UserFollows
from .forms import NewTicketForm, NewUserForm


def home(request):
    """
    returns the main posts and reviews of the user and users followed.

    Parameter :
        request : HTTPrequest
    Returns :
        request : HTTPrequest
        context : Dict
        template : HTML page

    """
    if(request.user.is_authenticated):
        list_posts_and_reviews = []
        list_id_posts = []
        l_post_and_rev = []
        list_users_followed = UserFollows.objects.filter(user_id=request.user.id)
        list_reviews = Review.objects.all()
        list_posts = Ticket.objects.all()
        for r in list_reviews:
            p = Ticket.objects.filter(id=r.ticket_id)
            list_id_posts.append(p[0].id)
            l_post_and_rev.append({"post": p[0], "review": r, "has_one": 1})
        for p in list_posts:
            if p.id in list_id_posts:
                l_post_and_rev.append({"post": p, "review": None, "has_one": 1})
            else:
                l_post_and_rev.append({"post": p, "review": None, "has_one": 0})
        print(l_post_and_rev.__len__())
        for el in l_post_and_rev:
            print(el)
            if el["post"].user_id == request.user.id:
                list_posts_and_reviews.append(el)
            elif el["review"] is not None:
                if el['review'].user_id == request.user.id:
                    list_posts_and_reviews.append(el)
            if list_users_followed is not None:
                for e in list_users_followed:
                    if el["post"].user_id == e.followed_user_id and el not in list_posts_and_reviews:
                        list_posts_and_reviews.append(el)
                    elif el["review"] is not None:
                        if (el["review"].user_id == e.followed_user_id and el not in list_posts_and_reviews):
                            list_posts_and_reviews.append(el)
            print(list_posts_and_reviews.__len__())
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
    """
    creates a new user
    Parameter :
        request : HTTPrequest
    Returns :
        request : HTTPrequest
        context : Dict
        template : HTML page
    """
    if request.method == "POST":
        register_form = NewUserForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(request.POST)
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
    """
    login a user
    Parameter :
        request : HTTPrequest
    Returns :
        request : HTTPrequest
        context : Dict
        template : HTML page

    """
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
    """
    authenticate an user
    Parameter :
        request : HTTPrequest
    Returns :
        request : HTTPrequest
        context : Dict
        template : HTML page
    """
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
    """
    logout an user
    Parameter :
        request : HTTPrequest
    Returns :
        request : HTTPrequest
    """
    if(request is not None):
        auth.logout(request)
    return redirect("connection")


def create_ticket(request):
    """
    creates a ticket or post
    Parameter :
        request : HTTPrequest
    Returns :
        request : HTTPrequest
        context : Dict
        template : HTML page
    """
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
    """
    shows list of user's posts
    Parameter :
        request : HTTPrequest
    Returns :
        request : HTTPrequest
        context : Dict
        template : HTML page
    """
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
    """
    delete a post or ticket
    Parameter :
        request : HTTPrequest
        post_id : str
            the id of the post
    Returns :
        template : HTML page
    """
    post_to_del = Ticket.objects.get(id=post_id)
    post_to_id = post_to_del.user
    if(post_to_id == request.user):
        post_to_del.delete()
    return redirect("posts")


def update_ticket(request, post_id):
    """
    update a post or a ticket
    Parameter :
        request : HTTPrequest
        post_id : str
            the id of the post
    Returns :
        template : HTML page
    """
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
