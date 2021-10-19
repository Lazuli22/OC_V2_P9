from django.shortcuts import render

from core.models import Ticket


def posts(request):
    if request.method == "GET":
        list_posts = Ticket.objects.filter(user_id=request.user.id)
        return render(
            request,
            template_name="posts.html",
            context={
                'my_posts': list_posts,
            })