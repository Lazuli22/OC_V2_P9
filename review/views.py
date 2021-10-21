from django.shortcuts import render

from core.models import Ticket
from core.forms import NewTicketForm

def posts(request):
    list_posts = []
    if request.method == "GET":
        list_posts = Ticket.objects.filter(user_id=request.user.id)
    return render(
        request,
        template_name="posts.html",
        context={
                'my_posts': list_posts,
        })


def delete_post(request, post_id):
    post_to_del = Ticket.objects.get(id=post_id)
    post_to_del.delete()
    return posts(request)
    

def modify_post(request, post_id):
    post_to_modify = Ticket.objects.get(id=post_id)
    ticket_form = NewTicketForm()
    ticket_form.ticket = post_to_modify.ticket
    ticket_form.description = post_to_modify.description
    ticket_form.image = post_to_modify.image
    return render(
            request=request,
            template_name="modify_post.html",
            context={"ticket_form": ticket_form})

