# from django.shortcuts import render
# Create your views here.

from django.shortcuts import render

from core.models import User
from userfollows.models import UserFollows
from .forms import UserForm


def listing(request):
    if request.method == "POST":
        form = UserForm(request.POST, user=request.user)
    else:
        form = UserForm(user=request.user)
    context = {"form": form}
    followedUsers = UserFollows.objects.filter(user=request.user)
    followedUserObj = []
    for e in followedUsers:
        id_user = e.followed_user_id
        followedUserObj.append(User.objects.get(id=id_user).username)
    context["followedUserObj"] = followedUserObj
    followers = UserFollows.objects.filter(followed_user_id=request.user)
    followersObj = []
    for e in followers:
        id_user = e.user_id
        followersObj.append(User.objects.get(id=id_user).username)
    context["followersObj"] = followersObj
    return render(request, "follows.html", context)


def search(request):
    if request.method == "POST":
        form = UserForm(request.POST, user=request.user)
        context = {"form": form}
        option_value = request.POST.getlist('user_list')
        if option_value is not None:
            user_chosen = User.objects.get(username=option_value[0])
            context["user_chosen"] = user_chosen
            b = UserFollows(user=request.user, followed_user=user_chosen)
            b.save()
    return listing(request)


def unsubscribe(request, username):
    userTodel = User.objects.get(username=username)
    userFollowstoDel = UserFollows.objects.get(
        followed_user_id=userTodel.id, user_id=request.user.id
        )
    userFollowstoDel.delete()
    return listing(request)
